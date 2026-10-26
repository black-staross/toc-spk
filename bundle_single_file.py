import json

print("Bundling toeic_single_file.html...")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Inline CSS
css_tag = f"<style>\n{css}\n</style>"
html = html.replace('<link rel="stylesheet" href="style.css">', css_tag)

# Inline Master Data and App JS
data_json_str = json.dumps(data, ensure_ascii=False)
js_bundle = f"""<script>
window.TOEIC_MASTER_DATA = {data_json_str};
{js}
</script>"""

html = html.replace('<script src="app.js"></script>', js_bundle)

with open('toeic_single_file.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Successfully generated toeic_single_file.html (Size: {len(html):,} bytes)")
