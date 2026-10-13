import urllib.request
import re
import json

base_url = "https://www.adelgroup.vn"
categories = [
    {"name": "Khóa vân tay", "slug": "khoa-van-tay", "url": "/khoa-van-tay/"},
    {"name": "Khóa Push Pull", "slug": "khoa-push-pull", "url": "/khoapushpull/"},
    {"name": "Khóa vân tay cửa nhôm", "slug": "khoa-cua-nhom", "url": "/khoa-van-tay-cua-nhom/"},
    {"name": "Khóa mã số", "slug": "khoa-ma-so", "url": "/khoa-ma-so/"},
    {"name": "Khóa cửa kính, deadbolt", "slug": "khoa-cua-kinh", "url": "/khoa-cua-kinh-deadbolt/"},
    {"name": "Khóa cổng", "slug": "khoa-cong", "url": "/khoa-cong/"},
    {"name": "Khóa khách sạn", "slug": "khoa-khach-san", "url": "/khoa-khach-san/"}
]

all_products = []
seen = set()

for cat in categories:
    url = base_url + cat["url"]
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        
        # Match each <li> containing <div class="thumb"> and <div class="info">
        li_matches = re.findall(r'<li>\s*<div class="thumb"><a href="([^"]+)"><img src="([^"]+)"[^>]*alt="([^"]*)"[\s\S]*?<h2><a[^>]*>([^<]+)</a></h2>\s*<p><span class="price">([^<]+)</span>', html)
        for link, img, alt, name, price in li_matches:
            name_clean = name.strip()
            if name_clean and name_clean not in seen:
                seen.add(name_clean)
                all_products.append({
                    "id": f"adel-{len(all_products)+1:03d}",
                    "name": name_clean,
                    "brand": "ADEL",
                    "category": "khoa-dien-tu",
                    "subCategory": cat["slug"],
                    "categoryName": cat["name"],
                    "price": price.replace("&nbsp;", " ").strip(),
                    "image": base_url + img if img.startswith('/') else img,
                    "link": base_url + link if link.startswith('/') else link,
                    "badge": "Chính hãng ADEL"
                })
    except Exception as e:
        pass

# Add future categories: Thiết bị vệ sinh & Nội thất để Vương Tín hoàn chỉnh hệ sinh thái
sanitary_products = [
    {
        "id": "tbvs-001",
        "name": "Bồn Cầu Thông Minh Vương Tín VT-Smart 8800",
        "brand": "Vương Tín",
        "category": "thiet-bi-ve-sinh",
        "subCategory": "bon-cau-thong-minh",
        "categoryName": "Bồn Cầu Thông Minh",
        "price": "14,500,000 đ",
        "image": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80",
        "badge": "Công nghệ Nano"
    },
    {
        "id": "tbvs-002",
        "name": "Lavabo Đá Tự Nhiên Liền Khối VT-LV09 Luxury",
        "brand": "Vương Tín",
        "category": "thiet-bi-ve-sinh",
        "subCategory": "lavabo",
        "categoryName": "Chậu Lavabo",
        "price": "4,200,000 đ",
        "image": "https://images.unsplash.com/photo-1620626011761-996317b8d101?auto=format&fit=crop&w=600&q=80",
        "badge": "Men sứ kháng khuẩn"
    },
    {
        "id": "tbvs-003",
        "name": "Bồn Cầu Trứng 1 Khối Men Tuyết VT-Egg 66",
        "brand": "Vương Tín",
        "category": "thiet-bi-ve-sinh",
        "subCategory": "bon-cau",
        "categoryName": "Bồn Cầu 1 Khối",
        "price": "5,800,000 đ",
        "image": "https://images.unsplash.com/photo-1564540574859-0dfb63985953?auto=format&fit=crop&w=600&q=80",
        "badge": "Tiết kiệm nước"
    },
    {
        "id": "tbvs-004",
        "name": "Sen Tắm Cây Nhiệt Độ Phím Đàn VT-Piano Black",
        "brand": "Vương Tín",
        "category": "thiet-bi-ve-sinh",
        "subCategory": "sen-tam",
        "categoryName": "Sen Vòi & Phụ Kiện",
        "price": "3,650,000 đ",
        "image": "https://images.unsplash.com/photo-1585058177579-24b893bb0b4b?auto=format&fit=crop&w=600&q=80",
        "badge": "Đồng mạ PVD"
    }
]

furniture_products = [
    {
        "id": "nt-001",
        "name": "Bộ Bàn Ăn Mặt Đá Ceramic Chống Xước 6 Ghế Monet",
        "brand": "Vương Tín",
        "category": "noi-that",
        "subCategory": "ban-ghe-an",
        "categoryName": "Bàn Ghế Ăn",
        "price": "12,800,000 đ",
        "image": "https://images.unsplash.com/photo-1617806118233-18e1de247200?auto=format&fit=crop&w=600&q=80",
        "badge": "Chống ố cao cấp"
    },
    {
        "id": "nt-002",
        "name": "Sofa Da Ý Phòng Khách Cao Cấp VT-Milano 3M",
        "brand": "Vương Tín",
        "category": "noi-that",
        "subCategory": "sofa-phong-khach",
        "categoryName": "Sofa & Bàn Trà",
        "price": "21,500,000 đ",
        "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=600&q=80",
        "badge": "Khung gỗ sồi"
    },
    {
        "id": "nt-003",
        "name": "Tủ Giày Thông Minh Cửa Lùa Cảm Ứng Đèn Led",
        "brand": "Vương Tín",
        "category": "noi-that",
        "subCategory": "tu-ke-thong-minh",
        "categoryName": "Tủ & Kệ Gia Đình",
        "price": "4,900,000 đ",
        "image": "https://images.unsplash.com/photo-1595428774223-ef52624120d2?auto=format&fit=crop&w=600&q=80",
        "badge": "Gỗ MDF chống ẩm"
    }
]

catalog_data = {
    "siteName": "VƯƠNG TÍN",
    "slogan": "Tổng Kho Khóa Điện Tử ADEL & Nội Thất Thiết Bị Vệ Sinh Cao Cấp",
    "hotline": "0903 354 397",
    "hotline2": "0988 888 888",
    "email": "kinhdoanh@vuongtin.vn",
    "address": "Showroom Vương Tín - Hệ Thống Phân Phối Toàn Quốc",
    "adel_products": all_products,
    "sanitary_products": sanitary_products,
    "furniture_products": furniture_products
}

with open("products_data.json", "w", encoding="utf-8") as f:
    json.dump(catalog_data, f, ensure_ascii=False, indent=2)

print(f"Extraction finished! Total ADEL: {len(all_products)}, Sanitary: {len(sanitary_products)}, Furniture: {len(furniture_products)}")
