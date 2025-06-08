from pathlib import Path
from html.parser import HTMLParser

class ScriptSrcParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            attrs = dict(attrs)
            if 'src' in attrs:
                self.scripts.append(attrs['src'])

HTML_FILES = ['public/index.html', 'public/sign.html', 'public/evm.html', 'public/solana.html']

def test_config_script_present():
    for file in HTML_FILES:
        html = Path(file).read_text()
        parser = ScriptSrcParser()
        parser.feed(html)
        assert 'config.js' in parser.scripts, f"config.js missing in {file}"
