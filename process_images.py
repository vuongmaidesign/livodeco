import os
import json
import urllib.request
from PIL import Image
import numpy as np

os.makedirs("images/products_png", exist_ok=True)

with open("products_data.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

adel_prods = catalog.get("adel_products", [])
print(f"Total ADEL products to process transparent PNG: {len(adel_prods)}")

headers = {'User-Agent': 'Mozilla/5.0'}

for idx, p in enumerate(adel_prods):
    img_url = p["image"]
    slug = p["slug"]
    out_png_path = f"images/products_png/{slug}.png"

    if os.path.exists(out_png_path) and os.path.getsize(out_png_path) > 1000:
        p["image"] = out_png_path
        continue

    try:
        req = urllib.request.Request(img_url, headers=headers)
        raw_data = urllib.request.urlopen(req, timeout=10).read()
        
        # Open image
        from io import BytesIO
        img = Image.open(BytesIO(raw_data)).convert("RGBA")
        
        data = np.array(img)
        # Find pixels that are white or near white (r > 240, g > 240, b > 240)
        # Note: also remove the small blue wifi watermark if near top right corner
        h, w, c = data.shape
        r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
        
        # White background condition
        white_mask = (r > 238) & (g > 238) & (b > 238)
        
        # Erase watermarks near top-right corner if needed (x > w*0.75, y < h*0.25)
        # If blue icon in corner
        corner_y = int(h * 0.22)
        corner_x = int(w * 0.70)
        blue_icon_mask = np.zeros((h, w), dtype=bool)
        blue_icon_mask[:corner_y, corner_x:] = (b > 150) & (r < 100) # blue color
        
        data[white_mask, 3] = 0
        data[blue_icon_mask, 3] = 0
        
        # Convert back and save
        clean_img = Image.fromarray(data)
        clean_img.save(out_png_path, "PNG", optimize=True)
        
        p["image"] = out_png_path
        if (idx + 1) % 15 == 0:
            print(f"Processed {idx + 1}/{len(adel_prods)} transparent PNGs...")
    except Exception as e:
        print(f"Error {slug}: {e}")

with open("products_data.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

js_bundle = "window.VUONGTIN_DATA = " + json.dumps(catalog, ensure_ascii=False) + ";"
with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_bundle)

print("SUCCESS: Converted all product images into clean transparent PNGs!")
