import json
import base64
import io
from PIL import Image, ImageFilter

print("Upscaling all 26 Part 2 photos to High-Res (800x570 with Lanczos & UnsharpMask)...")

with open('data.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

img_dir = '/Users/sanghyeonpark/.gemini/users/user2/toeic_part2_images'

for i, q in enumerate(master.get("part2", [])):
    qid = q.get("id", i + 1)
    filename = f"part2_q{qid:02d}_photo.jpg"
    filepath = f"{img_dir}/{filename}"
    
    try:
        im = Image.open(filepath)
        # 2.5x upscale to ~800x570
        new_w = int(im.width * 2.5)
        new_h = int(im.height * 2.5)
        im_upscaled = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
        # Apply crisp unsharp mask for clarity
        im_sharp = im_upscaled.filter(ImageFilter.UnsharpMask(radius=1.8, percent=135, threshold=2))
        
        # Save to buffer as high-quality JPEG
        buf = io.BytesIO()
        im_sharp.save(buf, format="JPEG", quality=92, optimize=True)
        buf.seek(0)
        
        b64_data = base64.b64encode(buf.read()).decode('utf-8')
        data_uri = f"data:image/jpeg;base64,{b64_data}"
        
        q["imageUrl"] = data_uri
        print(f"Processed Q{qid:02d}: {im.size} -> {im_sharp.size} (Base64 length: {len(data_uri)})")
    except Exception as e:
        print(f"Error processing Q{qid}: {e}")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

print("Successfully updated all 26 photos in data.json with High-Res Base64!")
