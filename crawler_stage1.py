import urllib.request
import re
import json
import time

base_url = "https://www.adelgroup.vn"

# List of main sections & sub-sections on adelgroup.vn
category_urls = [
    {"url": "/khoa-van-tay/", "cat": "khoa-van-tay", "catName": "Khóa Vân Tay Tay Gạt"},
    {"url": "/khoapushpull/", "cat": "khoa-push-pull", "catName": "Khóa Push-Pull Hiện Đại"},
    {"url": "/khoa-van-tay-cua-nhom/", "cat": "khoa-cua-nhom", "catName": "Khóa Cửa Nhôm Kính Xingfa"},
    {"url": "/khoa-ma-so/", "cat": "khoa-ma-so", "catName": "Khóa Mã Số Điện Tử"},
    {"url": "/khoa-cua-kinh-deadbolt/", "cat": "khoa-cua-kinh", "catName": "Khóa Cửa Kính & Deadbolt"},
    {"url": "/khoa-cong/", "cat": "khoa-cong", "catName": "Khóa Cổng Chống Nước"},
    {"url": "/khoa-khach-san/", "cat": "khoa-khach-san", "catName": "Khóa Khách Sạn & Thẻ Từ"},
    {"url": "/danh-muc-khoa-khach-san/", "cat": "khoa-khach-san", "catName": "Danh Mục Khóa Khách Sạn"},
    {"url": "/phu-kien-khoa-van-tay-khach-san/", "cat": "phu-kien-khoa", "catName": "Phụ Kiện Khóa Khách Sạn"}
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        return urllib.request.urlopen(req, timeout=12).read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# Step 1: Collect all product links from categories (including pagination if any)
discovered_products = []
seen_links = set()

for c in category_urls:
    first_url = base_url + c["url"]
    html = fetch_url(first_url)
    if not html:
        continue
    
    # Check pagination links like ?p=2 or page=2
    pages = [first_url]
    page_matches = re.findall(r'href="([^"]*(?:page|\?p=|\&p=)[^"]*)"', html)
    for pm in page_matches:
        full_p = base_url + pm if pm.startswith('/') else pm
        if full_p not in pages and c["url"] in full_p:
            pages.append(full_p)
            
    for p_url in pages:
        p_html = fetch_url(p_url) if p_url != first_url else html
        # Extract product cards
        # <li><div class="thumb"><a href="...">...</a></div><div class="info"><h2><a href="...">...</a></h2><p><span class="price">...</span>
        items = re.findall(r'<li>\s*<div class="thumb"><a href="([^"]+)"><img src="([^"]+)"[^>]*alt="([^"]*)"[\s\S]*?<h2><a[^>]*>([^<]+)</a></h2>\s*<p><span class="price">([^<]+)</span>', p_html)
        print(f"Cat {c['cat']}: found {len(items)} items on {p_url}")
        
        for link, img, alt, name, price in items:
            name_clean = name.strip()
            link_clean = link.strip()
            if link_clean not in seen_links:
                seen_links.add(link_clean)
                discovered_products.append({
                    "name": name_clean,
                    "rel_link": link_clean,
                    "detail_url": base_url + link_clean if link_clean.startswith('/') else link_clean,
                    "image": base_url + img if img.startswith('/') else img,
                    "price": price.replace("&nbsp;", " ").strip(),
                    "category": c["cat"],
                    "categoryName": c["catName"]
                })

print(f"Total discovered ADEL products: {len(discovered_products)}")
with open("discovered_products.json", "w", encoding="utf-8") as f:
    json.dump(discovered_products, f, ensure_ascii=False, indent=2)
