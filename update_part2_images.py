import json

print("Updating Part 2 with high-res real exam photo URLs in data.json...")

with open('data.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

photo_urls = {
    1: "https://images.unsplash.com/photo-1578916171728-46686eac8d58?auto=format&fit=crop&w=1200&q=80", # Grocery Store
    2: "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1200&q=80", # Retail Store
    3: "https://images.unsplash.com/photo-1556742049-0a67c5574f73?auto=format&fit=crop&w=1200&q=80", # Checkout Counter Card
    4: "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1200&q=80", # Hotel Front Desk
    5: "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80", # Restaurant Table Dining
    6: "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=1200&q=80", # Cafe Cake & Menu
    7: "https://images.unsplash.com/photo-1519331379826-f10be5486c6f?auto=format&fit=crop&w=1200&q=80", # Outdoor Park Walk & Call
    8: "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1200&q=80", # Park Trail & Bench
    9: "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=1200&q=80", # Classic Library
    10: "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&w=1200&q=80", # Classroom Handouts
    11: "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80", # Office Lounge Suit
    12: "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80", # Lounge Device Multitasking
    13: "https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?auto=format&fit=crop&w=1200&q=80", # Flea Market Cameras
    14: "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=1200&q=80"  # Cafe Counter Barista
}

for q in master.get("part2", []):
    s_id = q.get("setId") or q.get("setNumber") or 1
    q["imageUrl"] = photo_urls.get(s_id, photo_urls[1])

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

print("Successfully injected 14 high-res real photo URLs into data.json!")
