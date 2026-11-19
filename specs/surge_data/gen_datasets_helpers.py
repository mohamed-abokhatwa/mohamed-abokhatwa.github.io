"""Helpers shared with gen_datasets.py (dec_group keeps each bucket's extremes)."""
def dec_group(t, series, n=260):
    """Reduce a set of series that share one time axis to about n samples WITHOUT losing their
    extremes: every bucket keeps its first index plus the argmin and argmax of each series, so a
    plotted trace reaches the same peak as the full-resolution envelope and all series stay aligned."""
    m = len(t)
    if m <= n: return t, list(series)
    nb = max(1, n//(1 + len(series))); step = m/nb; idx = set()
    for b in range(nb):
        i0 = int(b*step); i1 = min(m, int((b+1)*step))
        if i1 <= i0: continue
        idx.add(i0)
        for y in series:
            seg = y[i0:i1]
            idx.add(i0 + min(range(len(seg)), key=lambda k: seg[k]))
            idx.add(i0 + max(range(len(seg)), key=lambda k: seg[k]))
    idx.add(m-1)
    ii = sorted(idx)
    return [t[i] for i in ii], [[y[i] for i in ii] for y in series]
def dec(arr, n=260):
    """Single series with no partner axis (kept for compatibility): plain stride reduction."""
    if len(arr) <= n: return arr
    step = len(arr)/n
    return [arr[int(i*step)] for i in range(n)]
def r1(a): return [round(v, 1) for v in a]
def r2l(a): return [round(v, 2) for v in a]   # envelopes: stored at the precision the lengths above a limit are measured at
def r2(v): return round(v, 2)
