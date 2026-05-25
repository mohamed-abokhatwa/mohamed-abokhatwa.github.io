/* theme.js — Dark / Light Mode
   Included at the bottom of every page.
   The critical flash-prevention snippet is inlined in <head>:
     (function(){var t=localStorage.getItem('site-theme')||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');document.documentElement.setAttribute('data-theme',t);})();
*/

(function () {
  'use strict';

  function applyTheme(t) {
    document.documentElement.setAttribute('data-theme', t);
    localStorage.setItem('site-theme', t);
    var btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.setAttribute('aria-label', t === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
      btn.setAttribute('title',       t === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
  }

  window.toggleTheme = function () {
    var current = document.documentElement.getAttribute('data-theme') || 'light';
    applyTheme(current === 'dark' ? 'light' : 'dark');
  };

  /* Set initial aria-label once DOM is ready */
  document.addEventListener('DOMContentLoaded', function () {
    var t   = document.documentElement.getAttribute('data-theme') || 'light';
    var btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.setAttribute('aria-label', t === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
      btn.setAttribute('title',       t === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
  });
})();
