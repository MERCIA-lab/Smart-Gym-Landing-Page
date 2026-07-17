#!/usr/bin/env python3
import re
import hashlib
from pathlib import Path
from urllib.request import urlopen, Request
import shutil
import subprocess

root = Path(__file__).resolve().parent.parent
images_dir = root / 'images'
images_dir.mkdir(exist_ok=True)
html_files = [p for p in root.glob('*.html') if p.is_file()]
pattern = re.compile(r'(https?://(?:images\.unsplash\.com|source\.unsplash\.com)/[^"\'>\s]+)')

url_map = {}

for path in html_files:
    text = path.read_text(encoding='utf-8')
    for m in pattern.finditer(text):
        url = m.group(1)
        if url not in url_map:
            h = hashlib.sha1(url.encode('utf-8')).hexdigest()[:12]
            fname = f'unsplash-{h}.jpg'
            url_map[url] = fname

print('Found', len(url_map), 'unique remote images')

for url, fname in url_map.items():
    out_path = images_dir / fname
    if out_path.exists():
        print('Skipping existing', fname)
        continue
    try:
        print('Downloading', url)
        req = Request(url, headers={'User-Agent': 'curl/7.0'})
        with urlopen(req, timeout=30) as resp, open(out_path, 'wb') as out:
            shutil.copyfileobj(resp, out)
        # convert/resize using sips (macOS)
        print('Optimizing', fname)
        subprocess.run(['sips', '-s', 'format', 'jpeg', str(out_path), '--out', str(out_path)], check=False)
        subprocess.run(['sips', '-Z', '1200', str(out_path)], check=False)
    except Exception as e:
        print('Error fetching', url, e)

# Update HTML files to use local images and add loading="lazy"
for path in html_files:
    text = path.read_text(encoding='utf-8')
    new = text
    for url, fname in url_map.items():
        new = new.replace(f'src="{url}"', f'src="images/{fname}"')
        new = new.replace(f'href="{url}"', f'href="images/{fname}"')
    # add loading="lazy" to img tags missing it
    new = re.sub(r'<img([^>]*)>', lambda m: ('<img'+m.group(1)+ ' loading="lazy">') if 'loading=' not in m.group(1) else m.group(0), new)
    if new != text:
        path.write_text(new, encoding='utf-8')
        print('Updated', path.name)

print('Done')
