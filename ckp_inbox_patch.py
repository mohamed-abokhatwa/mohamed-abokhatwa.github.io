#!/usr/bin/env python3
"""CockpitPro Inbox wave: incremental AI triage + action brief, category filters,
user-set fetch count, proper HTML message rendering. Anchored regex edits with
count assertions; aborts before writing anything if any anchor is off."""
import re, sys, py_compile

ROOT = "/Users/abokhatwa/Documents/WORK/Cowork/Agents/Creat AI Agents/CockpitPro"
CR = ROOT + "/backend/cockpit/api/comms_routes.py"
MB = ROOT + "/backend/cockpit/integrations/mac_bridge.py"
TSX = ROOT + "/frontend/src/pages/Comms.tsx"

def load(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def save(p, s):
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)

edits_done = []

def sub1(text, pattern, repl, label, flags=0):
    hits = len(re.findall(pattern, text, flags))
    if hits != 1:
        print(f"ABORT {label}: {hits} matches for anchor")
        sys.exit(1)
    edits_done.append(label)
    return re.sub(pattern, repl, text, count=1, flags=flags)

# ---------------------------------------------------------------- comms_routes.py
cr = load(CR)

cr = sub1(cr, r"^import json$", "import hashlib\nimport json", "cr-import-hashlib", re.M)
cr = sub1(cr, r"^import re$", "import re\nimport urllib.parse", "cr-import-urllib", re.M)
cr = sub1(cr, r"from fastapi\.responses import StreamingResponse",
          "from fastapi.responses import FileResponse, StreamingResponse", "cr-import-fileresponse")

cr = sub1(cr,
          r'    except Exception:\n        res\["triage"\] = None\n    return res',
          '    except Exception:\n        res["triage"] = None\n    res["limit"] = lim\n    return res',
          "cr-inbox-limit-echo")

NEW_EPS = r'''MSG_ASSETS = config.APP_DATA / "msg_assets"

_CID_RX = re.compile(r'src=["\']cid:([^"\']+)["\']', re.I)
_SCRIPT_RX = re.compile(r"<script\b[^>]*>.*?</script>", re.I | re.S)
_ONATTR_RX = re.compile(r'\son\w+\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s>]+)', re.I)
_IMG_EXT = ("png", "jpg", "jpeg", "gif", "bmp", "webp", "tiff", "svg")


def _msg_cache_dir(msg_id: str) -> Path:
    h = hashlib.md5(str(msg_id).encode()).hexdigest()[:16]
    d = MSG_ASSETS / h
    d.mkdir(parents=True, exist_ok=True)
    return d


@router.get("/comms/message_html")
def message_html(msg_id: str = "", user: User = Depends(auth.current_user)):
    # Original HTML of a message (tables, formatting, embedded images).
    # Scripts/handlers stripped; cid: images served from a per-message cache.
    res = mb.outlook_message_html(msg_id)
    if not res.get("available"):
        raise HTTPException(503, res.get("reason", "unavailable"))
    html = res.get("html") or ""
    html = _SCRIPT_RX.sub("", html)
    html = _ONATTR_RX.sub("", html)
    cids = _CID_RX.findall(html)
    if cids:
        d = _msg_cache_dir(msg_id)
        have = {f.name for f in d.iterdir() if f.is_file()}
        if not have:
            att = mb.outlook_save_attachments(msg_id, d)
            if att.get("available"):
                have = {Path(f).name for f in att.get("files", [])}
        images = sorted(n for n in have
                        if "." in n and n.lower().rsplit(".", 1)[-1] in _IMG_EXT)
        used: set = set()

        def _pick(cid: str) -> str:
            base = cid.split("@")[0].lower()
            stem = base.rsplit(".", 1)[0]
            for n in images:
                nl = n.lower()
                if n not in used and base and (base in nl or nl in base or
                                               (stem and stem in nl)):
                    used.add(n)
                    return n
            for n in images:
                if n not in used:
                    used.add(n)
                    return n
            return ""

        mapping = {c: _pick(c) for c in dict.fromkeys(cids)}

        def _sub(mo):
            n = mapping.get(mo.group(1), "")
            if not n:
                return mo.group(0)
            return ('src="/api/comms/message_asset?msg_id='
                    + urllib.parse.quote(str(msg_id))
                    + "&name=" + urllib.parse.quote(n) + '"')

        html = _CID_RX.sub(_sub, html)
    return {"available": True, "subject": res.get("subject", ""),
            "from": res.get("from", ""), "html": html}


@router.get("/comms/message_asset")
def message_asset(msg_id: str = "", name: str = "",
                  user: User = Depends(auth.current_user)):
    d = _msg_cache_dir(msg_id)
    p = (d / Path(name).name).resolve()
    if not str(p).startswith(str(d.resolve())) or not p.is_file():
        raise HTTPException(404, "No such asset")
    return FileResponse(p)


'''
cr = sub1(cr, r'@router\.get\("/comms/message"\)\n',
          NEW_EPS.replace("\\", "\\\\") + '@router.get("/comms/message")\n',
          "cr-new-endpoints")

NEW_JOB = r'''    @handler("inbox_triage")
    def _job(ctx: JobContext) -> dict:
        lim = ctx.payload.get("limit") or int(config.settings.get("comms.inbox_limit", 30))
        ctx.progress(0.08, "Reading the inbox…")
        res = mb.outlook_inbox(lim)
        if not res.get("available"):
            raise RuntimeError(res.get("reason", "Outlook unavailable"))
        msgs = res["messages"]
        if not msgs:
            return {"summary": "Inbox is empty.", "link": "/comms"}

        # Incremental: reuse earlier classifications, classify only NEW mail.
        prev: dict = {}
        old_items: dict = {}
        try:
            prev = json.loads(TRIAGE_CACHE.read_text("utf-8"))
            for it in prev.get("items", []):
                old_items[str(it.get("id") or it.get("subject"))] = it
        except Exception:
            prev = {}

        def _key(m: dict) -> str:
            return str(m.get("id") or m.get("subject"))

        new_msgs = [(i, m) for i, m in enumerate(msgs) if _key(m) not in old_items]
        ctx.progress(0.3, f"Classifying {len(new_msgs)} new of {len(msgs)} messages…")
        by_n: dict = {}
        if new_msgs:
            digest = []
            for i, m in new_msgs:
                digest.append({"n": i, "subject": m["subject"], "from": m["from"],
                               "received": m["received"],
                               "attachments": m["attachments"][:5],
                               "body": m["body"][:700]})
            extra = ("Classify each inbox message. Return STRICT JSON only, an array of "
                     '{"n": <index>, "category": "urgent-action|action|awaiting-others|info|noise", '
                     '"reason": "<max 15 words>", "suggested_action": "<max 20 words or empty>"}.'
                     "\nMessages:\n" + json.dumps(digest, ensure_ascii=False))
            events: list = []
            out = run_brain("Classify these messages now. JSON array only, no prose.",
                            [], lambda ev: events.append(ev), extra_system=extra)
            try:
                m0 = re.search(r"\[.*\]", out.get("text", ""), re.S)
                classes = json.loads(m0.group(0)) if m0 else []
            except Exception:
                classes = []
            by_n = {c.get("n"): c for c in classes if isinstance(c, dict)}

        items = []
        for i, m in enumerate(msgs):
            kept = old_items.get(_key(m)) or {}
            c = by_n.get(i) or {}
            items.append({"subject": m["subject"], "from": m["from"],
                          "received": m["received"], "id": m["id"],
                          "attachments": m["attachments"],
                          "category": c.get("category") or kept.get("category", "info"),
                          "reason": c.get("reason") or kept.get("reason", ""),
                          "suggested_action": (c.get("suggested_action")
                                               or kept.get("suggested_action", ""))})
        order = {"urgent-action": 0, "action": 1, "awaiting-others": 2, "info": 3, "noise": 4}
        items.sort(key=lambda x: order.get(x["category"], 3))
        counts = {k: sum(1 for x in items if x["category"] == k) for k in order}

        # The action brief: recommendations + insights over what needs attention.
        brief = (prev or {}).get("brief")
        if new_msgs or not brief:
            ctx.progress(0.62, "Writing the brief…")
            need = [x for x in items
                    if x["category"] in ("urgent-action", "action", "awaiting-others")]
            refs = sorted({x.upper().replace(" ", "-")
                           for m in msgs
                           for x in _REF_RX.findall((m.get("subject") or "") + " "
                                                    + (m.get("body") or ""))})[:10]
            reg_lines = []
            if refs:
                try:
                    from .. import registers
                    for ref in refs:
                        for rt in ("rfi", "submittal", "deadline"):
                            rows, _t = registers.list_items(rt, q=ref, limit=2)
                            for row in rows:
                                reg_lines.append(
                                    f"{ref} [{rt}]: "
                                    + json.dumps(row, ensure_ascii=False, default=str)[:280])
                except Exception:
                    pass
            b_extra = ("Write an ACTION BRIEF of this inbox for the workspace owner "
                       "(a mechanical construction manager). Return STRICT JSON only: "
                       '{"headline": "<max 14 words>", "overview": "<2 short sentences>", '
                       '"recommendations": [{"subject": "<exact message subject>", '
                       '"text": "<what to do, max 22 words>"}], '
                       '"insights": ["<max 20 words each>"], '
                       '"waiting_on": [{"who": "", "what": "<max 12 words>"}]} '
                       "— 3 to 6 recommendations for the most consequential messages only; "
                       "insights = deadlines spotted, patterns, risks; use the register "
                       "lines for the live status of items mentioned in mail.\n"
                       "Messages needing attention:\n"
                       + json.dumps([{"subject": x["subject"], "from": x["from"],
                                      "received": x["received"],
                                      "category": x["category"], "reason": x["reason"],
                                      "suggested_action": x["suggested_action"]}
                                     for x in need[:25]], ensure_ascii=False)
                       + "\nCounts: " + json.dumps(counts)
                       + ("\nRegister status lines:\n" + "\n".join(reg_lines)
                          if reg_lines else ""))
            ev2: list = []
            out2 = run_brain("Write the action brief now. JSON only, no prose.",
                             [], lambda ev: ev2.append(ev), extra_system=b_extra)
            try:
                m1 = re.search(r"\{.*\}", out2.get("text", ""), re.S)
                brief = json.loads(m1.group(0)) if m1 else None
            except Exception:
                brief = None

        ctx.progress(0.9, "Compiling triage…")
        result = {"at": dt.datetime.now().isoformat(timespec="minutes"),
                  "mode": ("cached" if not new_msgs else
                           ("incremental" if old_items else "full")),
                  "new": len(new_msgs), "items": items, "counts": counts,
                  "brief": brief}
        TRIAGE_CACHE.write_text(json.dumps(result, ensure_ascii=False, indent=1), "utf-8")
        urgent = counts.get("urgent-action", 0) + counts.get("action", 0)
        return {"summary": (f"{len(items)} messages · {len(new_msgs)} newly triaged · "
                            f"{urgent} need action"),
                "link": "/comms"}


_register_triage_job()'''

cr = sub1(cr, r'    @handler\("inbox_triage"\)\n    def _job.*?\n_register_triage_job\(\)',
          NEW_JOB.replace("\\", "\\\\"), "cr-triage-v2", re.S)
save(CR, cr)

# ---------------------------------------------------------------- mac_bridge.py
mb = load(MB)

NEW_MB = r'''def outlook_message_html(msg_id: str = "") -> Dict:
    # Original HTML content of one message (tables/images keep their layout).
    mid = str(msg_id or "").strip()
    if not mid.isdigit():
        return {"available": False, "reason": "No message id given.", "html": ""}
    script = f"""
    tell application "Microsoft Outlook"
      try
        set m to (first message of inbox whose id is {mid})
      on error
        return "__NOTFOUND__"
      end try
      set htmlText to ""
      try
        set htmlText to content of m
      end try
      if htmlText is "" then
        try
          set htmlText to plain text content of m
        end try
      end if
      set subj to ""
      try
        set subj to subject of m
      end try
      set theSender to ""
      try
        set theSender to (name of sender of m) & " <" & (address of sender of m) & ">"
      end try
      return subj & "{SEP}" & theSender & "{SEP}" & htmlText
    end tell
    """
    r = _osa(script, timeout=60)
    if not r["ok"]:
        return {"available": False, "reason": r["reason"], "html": ""}
    out = r["out"] or ""
    if out.strip() == "__NOTFOUND__":
        return {"available": False,
                "reason": "Message not found (it may have moved).", "html": ""}
    parts = out.split(SEP, 2)
    if len(parts) == 3:
        return {"available": True, "subject": parts[0], "from": parts[1],
                "html": parts[2]}
    return {"available": True, "subject": "", "from": "", "html": out}


'''
mbn = sub1(mb, r"\ndef outlook_save_attachments",
           "\n" + NEW_MB.replace("\\", "\\\\") + "def outlook_save_attachments",
           "mb-message-html")
save(MB, mbn)

# ---------------------------------------------------------------- Comms.tsx
tsx = load(TSX)

tsx = sub1(tsx, r"import React, \{ useState \} from 'react'",
           "import React, { useEffect, useRef, useState } from 'react'",
           "tsx-react-import")

NEW_TAB = r'''function InboxTab({ outlookUp }: { outlookUp?: boolean }) {
  const qc = useQueryClient()
  const { pushToast } = useApp()
  const inbox = useQuery({ queryKey: ['comms-inbox'], queryFn: () => api.get('/comms/inbox') })
  const [openMsg, setOpenMsg] = useState<any | null>(null)
  const [draftFor, setDraftFor] = useState<any | null>(null)
  const [catFilter, setCatFilter] = useState('all')
  const [q, setQ] = useState('')
  const autoRan = useRef(false)
  const triage = useMutation({
    mutationFn: () => api.post('/comms/inbox/triage', {}),
    onSuccess: () => pushToast({ kind: 'info', title: 'Triage started', body: 'New messages are being classified — the brief updates when it finishes.', link: '/jobs' }),
    onError: (e: any) => pushToast({ kind: 'error', title: 'Cannot triage', body: e.message }),
  })
  const saveKb = useMutation({
    mutationFn: (id: string) => api.post('/comms/save_to_kb', { msg_id: id }),
    onSuccess: (r) => pushToast({ kind: 'success', title: 'Saved into the knowledge base', body: r.saved.join('\n'), link: '/library' }),
    onError: (e: any) => pushToast({ kind: 'error', title: 'Save failed', body: e.message }),
  })
  const setLimit = useMutation({
    mutationFn: (n: number) => api.post('/settings', { patch: { comms: { inbox_limit: n } } }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['comms-inbox'] }),
    onError: (e: any) => pushToast({ kind: 'error', title: 'Could not save the count', body: e.message }),
  })
  const d = inbox.data
  // Auto-triage when the last run is older than 2 h (incremental server-side).
  useEffect(() => {
    if (!d?.available || autoRan.current || triage.isPending) return
    if (!(d?.messages || []).length) return
    const at = d?.triage?.at ? new Date(d.triage.at).getTime() : 0
    if (!at || Date.now() - at > 2 * 3600 * 1000) { autoRan.current = true; triage.mutate() }
  }, [d])
  // While a triage job runs, poll until the refreshed result lands (max 6 min).
  useEffect(() => {
    if (!triage.isSuccess) return
    const before = (qc.getQueryData(['comms-inbox']) as any)?.triage?.at || 'none'
    const t = setInterval(async () => {
      const r = await inbox.refetch()
      const now = (r.data as any)?.triage?.at || 'none'
      if (now !== before) clearInterval(t)
    }, 15000)
    const stop = setTimeout(() => clearInterval(t), 360000)
    return () => { clearInterval(t); clearTimeout(stop) }
  }, [triage.isSuccess])
  if (inbox.isLoading) return <div className="py-16 flex justify-center"><Spinner /></div>
  if (d && !d.available) {
    return <Empty icon={<Mail size={26} />} title="Outlook is not reachable"
                  sub={d.reason + (outlookUp === false ? ' — open Microsoft Outlook on the server Mac.' : '')}
                  action={<button className="btn btn-ghost" onClick={() => inbox.refetch()}><RefreshCw size={13} /> Retry</button>} />
  }
  const triaged: Record<string, any> = {}
  ;(d?.triage?.items || []).forEach((t: any) => { triaged[t.id || t.subject] = t })
  const cat = (m: any) => (triaged[m.id] || triaged[m.subject])?.category
  const CATC: Record<string, string> = {
    'urgent-action': 'text-bad', action: 'text-warn', 'awaiting-others': 'text-info',
    info: '', noise: 'text-ink3',
  }
  const CATS = ['urgent-action', 'action', 'awaiting-others', 'info', 'noise']
  const msgs = d?.messages || []
  const counts: Record<string, number> = { all: msgs.length }
  CATS.forEach(c => { counts[c] = msgs.filter((m: any) => cat(m) === c).length })
  const visible = msgs.filter((m: any) =>
    (catFilter === 'all' || cat(m) === catFilter) &&
    (!q || (m.subject + ' ' + m.from + ' ' + (m.body || '')).toLowerCase().includes(q.toLowerCase())))
  const brief = d?.triage?.brief
  return (
    <>
      <div className="flex items-center gap-2 flex-wrap">
        <span className="text-[12.5px] text-ink3 flex items-center gap-1.5">
          {visible.length === msgs.length ? `${msgs.length} messages` : `${visible.length} of ${msgs.length} messages`}
          <span>· fetch</span>
          <input className="input w-[64px] text-center" type="number" min={5} max={300}
                 key={d?.limit} defaultValue={d?.limit || 30} disabled={setLimit.isPending}
                 title="How many recent messages to read from Outlook"
                 onKeyDown={(e: any) => { if (e.key === 'Enter') e.currentTarget.blur() }}
                 onBlur={(e) => { const n = Math.max(5, Math.min(300, Math.round(Number(e.target.value) || 30))); if (n !== (d?.limit || 30)) setLimit.mutate(n) }} />
          {d?.triage && <span>· triaged {d.triage.at}{typeof d.triage.new === 'number' && d.triage.new > 0 ? ` (+${d.triage.new} new)` : ''}</span>}
        </span>
        <div className="ml-auto flex gap-2">
          <button className="btn btn-ghost btn-sm" onClick={() => inbox.refetch()}><RefreshCw size={13} /></button>
          <button className="btn btn-primary btn-sm" disabled={triage.isPending}
                  onClick={() => triage.mutate()}>
            <Sparkles size={13} /> AI triage
          </button>
        </div>
      </div>
      {brief && (
        <Card>
          <div className="flex items-start gap-2">
            <Sparkles size={15} className="text-brandhi mt-0.5 shrink-0" />
            <div className="min-w-0">
              <div className="text-[13.5px] font-semibold">{brief.headline}</div>
              {brief.overview && <div className="text-[12.5px] text-ink2 mt-0.5">{brief.overview}</div>}
              {(brief.recommendations || []).length > 0 && (
                <div className="mt-2 space-y-1">
                  {(brief.recommendations || []).map((r: any, i: number) => {
                    const mm = msgs.find((m: any) => m.subject === r.subject)
                    return (
                      <div key={i} className="text-[12.5px]">
                        <span className="text-brandhi font-semibold">{i + 1}.</span>{' '}
                        {mm
                          ? <button className="underline decoration-dotted underline-offset-2 hover:text-brandhi text-left" onClick={() => setOpenMsg(mm)}>{r.subject}</button>
                          : <span className="text-ink2">{r.subject}</span>}
                        <span className="text-ink2"> — {r.text}</span>
                      </div>
                    )
                  })}
                </div>
              )}
              {(brief.insights || []).length > 0 && (
                <div className="mt-2 space-y-0.5">
                  {(brief.insights || []).map((s: string, i: number) => (
                    <div key={i} className="text-[12px] text-ink2">💡 {s}</div>
                  ))}
                </div>
              )}
              {(brief.waiting_on || []).length > 0 && (
                <div className="mt-1.5 text-[12px] text-ink3">
                  ⏳ Waiting on: {(brief.waiting_on || []).map((w: any) => [w.who, w.what].filter(Boolean).join(' — ')).join(' · ')}
                </div>
              )}
            </div>
          </div>
        </Card>
      )}
      <div className="flex gap-1.5 flex-wrap items-center">
        {['all', ...CATS].map(c => (
          <button key={c} onClick={() => setCatFilter(c)}
                  className={cx('chip cursor-pointer', c !== 'all' && CATC[c],
                                catFilter === c && 'ring-1 ring-brandhi')}>
            {c === 'all' ? 'All' : c} ({counts[c] || 0})
          </button>
        ))}
        <input className="input ml-auto w-[190px]" placeholder="Search these messages…"
               value={q} onChange={(e) => setQ(e.target.value)} />
      </div>
      <Card pad={false}>
        <table className="w-full">
          <thead><tr><th>Message</th><th className="w-[150px]">From</th>
            <th className="w-[120px]">Category</th><th className="w-[210px]"></th></tr></thead>
          <tbody>
            {visible.map((m: any) => {
              const t = triaged[m.id] || triaged[m.subject]
              return (
                <tr key={m.id || m.subject}>
                  <td>
                    <button className="text-left hover:text-brandhi" onClick={() => setOpenMsg(m)}>
                      <div className="text-[13px] line-clamp-1">{m.subject}</div>
                    </button>
                    <div className="text-[11px] text-ink3 flex gap-1.5 flex-wrap mt-0.5">
                      {m.received}
                      {m.attachments.length > 0 && <span>· 📎 {m.attachments.length}</span>}
                      {m.refs?.map((r: string) => <span key={r} className="chip">{r}</span>)}
                    </div>
                    {t?.suggested_action && (
                      <div className="text-[11.5px] text-brandhi mt-0.5">→ {t.suggested_action}</div>
                    )}
                  </td>
                  <td className="text-[12px] text-ink3">{m.from}</td>
                  <td>{cat(m)
                    ? <button className={cx('chip', CATC[cat(m)])} title={t?.reason || ''}
                              onClick={() => setCatFilter(cat(m))}>{cat(m)}</button>
                    : <span className="text-[11px] text-ink3">—</span>}</td>
                  <td className="text-right">
                    <div className="flex justify-end gap-1.5">
                      <button className="btn btn-ghost btn-sm" title="Draft a reply (never sent)"
                              onClick={() => setDraftFor(m)}>Draft reply</button>
                      <button className="btn btn-ghost btn-sm" title="Save mail + attachments into the knowledge base"
                              disabled={saveKb.isPending}
                              onClick={() => saveKb.mutate(m.id)}>→ KB</button>
                    </div>
                  </td>
                </tr>
              )
            })}
            {visible.length === 0 && (
              <tr><td colSpan={4}>
                <div className="text-[12px] text-ink3 py-6 text-center">Nothing matches this filter.</div>
              </td></tr>
            )}
          </tbody>
        </table>
      </Card>
      {openMsg && <MessageModal m={openMsg} onClose={() => setOpenMsg(null)}
                                onDraft={() => { setDraftFor(openMsg); setOpenMsg(null) }} />}
      {draftFor && <DraftModal m={draftFor} onClose={() => setDraftFor(null)} />}
    </>
  )
}

function MessageModal({ m, onClose, onDraft }: any) {
  const rich = useQuery({
    queryKey: ['comms-msg-html', m.id],
    queryFn: () => api.get('/comms/message_html', { msg_id: m.id }),
    enabled: !!m.id, retry: 0,
  })
  const plain = useQuery({
    queryKey: ['comms-msg', m.id, m.subject],
    queryFn: () => api.get('/comms/message', { msg_id: m.id, subject: m.subject }),
    enabled: !m.id || rich.isError,
  })
  const html = rich.data?.html
  const doc = html ? `<!doctype html><html><head><meta charset="utf-8"><style>
    body{font:13px/1.55 -apple-system,'Segoe UI',sans-serif;color:#1c1c1e;margin:10px;background:#fff}
    img{max-width:100%;height:auto} table{border-collapse:collapse;max-width:100%}
    td,th{border:1px solid #ddd;padding:3px 6px} a{color:#00706A} blockquote{border-left:3px solid #ddd;margin-left:6px;padding-left:8px;color:#555}
  </style></head><body>${html}</body></html>` : ''
  return (
    <Modal open onClose={onClose} title={m.subject} wide>
      <div className="text-[12px] text-ink3 mb-2">{m.from} · {m.received}</div>
      {(rich.isLoading || (!html && plain.isLoading)) ? <Spinner />
        : html
          ? <iframe sandbox="allow-same-origin" srcDoc={doc} title="message"
                    className="w-full h-[56vh] bg-white border border-linesoft rounded-[10px]" />
          : <div className="text-[13px] leading-relaxed whitespace-pre-wrap max-h-[52vh] overflow-y-auto bg-panel2 border border-linesoft rounded-[10px] p-3">
              {plain.data?.body || '—'}
            </div>}
      <div className="flex justify-end gap-2 mt-3">
        <button className="btn btn-ghost" onClick={onClose}>Close</button>
        <button className="btn btn-primary" onClick={onDraft}>Draft a reply</button>
      </div>
    </Modal>
  )
}

'''
tsx = sub1(tsx, r"function InboxTab\(.*?\nfunction DraftModal\(",
           NEW_TAB.replace("\\", "\\\\") + "function DraftModal(", "tsx-inbox-tab", re.S)
save(TSX, tsx)

# ---------------------------------------------------------------- verify python
for p in (CR, MB):
    py_compile.compile(p, doraise=True)
print("PY_COMPILE_OK")
print("EDITS:", ",".join(edits_done))
