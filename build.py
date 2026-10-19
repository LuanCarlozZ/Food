"""Gera index.html (versão instalável/PWA) a partir de src/app.html.
Uso: python3 build.py"""
import pathlib
root = pathlib.Path(__file__).parent
frag = (root / "src" / "app.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0a110f">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-192.png">
<style>:root{color-scheme:light dark;padding-top:env(safe-area-inset-top,0px)}[hidden]{display:none!important}</style>
"""
tail = """
<script>
if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
  window.addEventListener('load', function () { navigator.serviceWorker.register('sw.js').catch(function () {}); });
  if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {});
}
</script>
</body></html>
"""
(root / "index.html").write_text(head + frag.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '') + tail, encoding="utf-8")
print("index.html gerado")
