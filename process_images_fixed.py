import os
import json
import urllib.request
from PIL import Image
import numpy as np

os.makedirs("images/products_png", exist_ok=True)

with open("products_data.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

adel_prods = catalog.get("adel_products", [])
print(f"Converting {len(adel_prods)} products to perfect transparent PNGs...")

headers = {'User-Agent': 'Mozilla/5.0'}

success_count = 0
for idx, p in enumerate(adel_prods):
    img_url = p.get("adel_url", "")
    # Use original image URL from ADEL if available or existing url
    src_url = p.get("original_image") or p["image"]
    if not src_url.startswith("http"):
        src_url = "https://www.adelgroup.vn" + src_url if src_url.startswith("/") else "https://www.adelgroup.vn/" + src_url

    slug = p["slug"]
    out_png_path = f"images/products_png/{slug}.png"

    try:
        req = urllib.request.Request(src_url, headers=headers)
        raw_data = urllib.request.urlopen(req, timeout=10).read()
        
        from io import BytesIO
        img = Image.open(BytesIO(raw_data)).convert("RGBA")
        data = np.array(img)
        
        h, w = data.shape[:2]
        r = data[:,:,0]
        g = data[:,:,1]
        b = data[:,:,2]
        
        # Condition 1: White/Off-white background (r>230, g>230, b>230)
        white_mask = (r > 230) & (g > 230) & (b > 230)
        data[white_mask, 3] = 0
        
        # Condition 2: Remove small blue wifi watermark in corner
        # Blue wifi watermark: blue > 140, red < 100, top right 25% area
        corner_y = int(h * 0.25)
        corner_x = int(w * 0.65)
        blue_mask = (b > 140) & (r < 100) & (g < 160)
        data[:corner_y, corner_x:][blue_mask[:corner_y, corner_x:], 3] = 0
        
        # Convert back & save
        clean_img = Image.fromarray(data)
        clean_img.save(out_png_path, "PNG", optimize=True)
        
        p["image"] = out_png_path
        success_count += 1
    except Exception as e:
        print(f"Error {slug}: {e}")

# Save updated JSON and data.js
with open("products_data.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

js_bundle = "window.VUONGTIN_DATA = " + json.dumps(catalog, ensure_ascii=False) + ";"
with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_bundle)

print(f"COMPLETED! Processed {success_count}/{len(adel_prods)} transparent PNG images.")
