from pathlib import Path

root = Path(__file__).resolve().parent.parent
images = root / 'images'
images.mkdir(exist_ok=True)

programs = {
    'program-strength.svg': ('Strength', 'barbell'),
    'program-hiit.svg': ('HIIT', 'flame'),
    'program-yoga.svg': ('Yoga', 'lotus'),
    'program-olympic.svg': ('Olympic', 'plate'),
    'program-crossfit.svg': ('CrossFit', 'kettlebell'),
    'program-bodybuilding.svg': ('Hypertrophy', 'arm'),
    'program-boxing.svg': ('Boxing', 'gloves'),
    'program-endurance.svg': ('Endurance', 'run'),
}

icons = {
    'barbell': '<rect x="120" y="140" width="260" height="40" rx="6" fill="#f5f5f5"/><rect x="80" y="120" width="40" height="80" rx="6" fill="#f5f5f5"/><rect x="380" y="120" width="40" height="80" rx="6" fill="#f5f5f5"/>',
    'flame': '<path d="M250 120c-10 30 10 50 10 80 10-30 40-40 40-80 0-30-40-40-50 0z" fill="#f5f5f5"/>',
    'lotus': '<path d="M250 120c-40 60-80 60-120 0 40-10 80-10 120 0z" fill="#f5f5f5"/><path d="M250 120c40 60 80 60 120 0-40-10-80-10-120 0z" fill="#f5f5f5"/>',
    'plate': '<circle cx="250" cy="170" r="48" fill="#f5f5f5"/><circle cx="250" cy="170" r="18" fill="#111"/>',
    'kettlebell': '<rect x="200" y="140" width="100" height="80" rx="18" fill="#f5f5f5"/><path d="M220 120a30 30 0 0 1 60 0" fill="#f5f5f5"/>',
    'arm': '<path d="M200 140c20-30 60-30 100 0-30 10-70 10-100 0z" fill="#f5f5f5"/><rect x="220" y="160" width="60" height="20" rx="6" fill="#f5f5f5"/>',
    'gloves': '<circle cx="210" cy="170" r="34" fill="#f5f5f5"/><circle cx="290" cy="170" r="34" fill="#f5f5f5"/>',
    'run': '<path d="M200 160c20-20 40-30 80-10-30 10-50 20-80 10z" fill="#f5f5f5"/><rect x="240" y="170" width="40" height="10" fill="#f5f5f5"/>',
}

template = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="600" height="360" viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="300" fill="#111"/>
  <rect x="16" y="16" width="468" height="268" rx="12" fill="#141414" stroke="#1f1f1f"/>
  <g transform="translate(0,0)">
    {icon}
  </g>
  <text x="250" y="260" text-anchor="middle" fill="#f5f5f5" font-family="Inter, system-ui, sans-serif" font-size="28">{label}</text>
</svg>
'''

for fname, (label, icon_key) in programs.items():
    content = template.format(icon=icons.get(icon_key, ''), label=label)
    (images / fname).write_text(content, encoding='utf-8')
    print('Wrote', fname)

# Replace existing program image references in HTML pages.
replacements = {
    'images/unsplash-fa0d5a62af03.jpg': 'images/program-strength.svg',
    'images/unsplash-dd03092e4e75.jpg': 'images/program-hiit.svg',
    'images/unsplash-0436519c6759.jpg': 'images/program-yoga.svg',
    'images/unsplash-990ae9bee4a9.jpg': 'images/program-olympic.svg',
    'images/unsplash-244887b1a4de.jpg': 'images/program-crossfit.svg',
    'images/unsplash-486bdc93ea5f.jpg': 'images/program-bodybuilding.svg',
    'images/unsplash-dc39367f914a.jpg': 'images/program-boxing.svg',
    'images/unsplash-bea06938822d.jpg': 'images/program-endurance.svg',
}

html_pages = [p for p in root.glob('*.html') if p.is_file()]
for page in html_pages:
    text = page.read_text(encoding='utf-8')
    new_text = text
    for old_src, new_src in replacements.items():
        new_text = new_text.replace(old_src, new_src)
    if new_text != text:
        page.write_text(new_text, encoding='utf-8')
        print('Patched', page.name)

print('SVG generation and HTML replacement complete.')
