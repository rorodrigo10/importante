"""Rebuild self-contained previews after changing checkout sources."""
from pathlib import Path
import base64
import re

root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text()
css = (root / 'style.css').read_text()

def embed_asset(match):
    data = base64.b64encode((root / match.group(1)).read_bytes()).decode()
    return "url('data:image/png;base64," + data + "')"

css = re.sub(r"url\('(assets/[^']+)'\)", embed_asset, css)
html = re.sub(r'<link rel="stylesheet" href="style.css[^\"]*">',
              lambda _: '<style>\n' + css + '\n</style>', html)
html = re.sub(r'<script src="app.js[^\"]*"></script>',
              lambda _: '<script>\n' + (root / 'app.js').read_text() + '\n</script>', html)
for filename in ('ABRIR-CHECKOUT.html', 'checkout-atualizado.html'):
    (root / filename).write_text(html)
