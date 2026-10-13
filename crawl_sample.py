import urllib.request
import re
import json

urls = [
    'https://www.adelgroup.vn/',
    'https://www.adelgroup.vn/khoa-van-tay/',
    'https://www.adelgroup.vn/khoapushpull/',
    'https://www.adelgroup.vn/khoa-khach-san/'
]

products = []
seen = set()

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        
        # Match product items
        # Pattern: thumb img src, link, title, price
        matches = re.findall(r'<div class="item">.*?<div class="thumb"><a href="([^"]*)"><img src="([^"]*)"[^>]*alt="([^"]*)"', html, re.DOTALL)
        for link, img, name in matches:
            if name not in seen:
                seen.add(name)
                # find price if nearby
                products.append({
                    'name': name.strip(),
                    'link': link,
                    'image': 'https://www.adelgroup.vn' + img if img.startswith('/') else img
                })
    except Exception as e:
        print(f"Error fetching {url}: {e}")

print(f"Found {len(products)} products")
with open("adel_products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)
print("Saved to adel_products.json")
