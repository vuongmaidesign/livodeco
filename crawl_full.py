import urllib.request
import re
import json

base_url = "https://www.adelgroup.vn"
categories = [
    "/khoa-van-tay/",
    "/khoapushpull/",
    "/khoa-van-tay-cua-nhom/",
    "/khoa-ma-so/",
    "/khoa-cua-kinh-deadbolt/",
    "/khoa-cong/",
    "/khoa-khach-san/"
]

all_products = []
seen = set()

for cat in categories:
    url = base_url + cat
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        
        # Regex for items
        items = re.findall(r'<div class="item">([\s\S]*?)</div>\s*</div>', html)
        for it in items:
            img_m = re.search(r'<img [^>]*src="([^"]+)"[^>]*alt="([^"]*)"', it)
            link_m = re.search(r'<h2><a href="([^"]+)">([^<]+)</a></h2>', it)
            price_m = re.search(r'<span class="price">([^<]+)</span>', it)
            
            if link_m:
                name = link_m.group(2).strip()
                link = link_m.group(1).strip()
                img = img_m.group(1).strip() if img_m else ""
                price = price_m.group(1).strip() if price_m else "Liên hệ"
                
                if name not in seen:
                    seen.add(name)
                    all_products.append({
                        "name": name,
                        "link": base_url + link if link.startswith('/') else link,
                        "image": base_url + img if img.startswith('/') else img,
                        "price": price,
                        "category": cat.strip('/')
                    })
    except Exception as e:
        print(f"Error {cat}: {e}")

print(f"Total ADEL products fetched: {len(all_products)}")
with open("adel_full_products.json", "w", encoding="utf-8") as f:
    json.dump(all_products, f, ensure_ascii=False, indent=2)
