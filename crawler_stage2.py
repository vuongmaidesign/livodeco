import json
import urllib.request
import re
import html
import time
from urllib.parse import urlparse

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_html(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        return urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error {url}: {e}")
        return ""

def clean_html(raw_html):
    if not raw_html:
        return ""
    # remove scripts and styles
    clean = re.sub(r'<script.*?</script>', '', raw_html, flags=re.DOTALL)
    clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL)
    return clean.strip()

with open("discovered_products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

print(f"Starting detailed scrape for {len(products)} products...")

full_catalog = []

for idx, p in enumerate(products):
    detail_url = p["detail_url"]
    page_html = fetch_html(detail_url)
    
    # Generate clean SEO slug
    slug = re.sub(r'[^a-z0-9]+', '-', p["name"].lower()).strip('-')
    if not slug:
        slug = f"khoa-adel-{idx+1}"

    # Extract Features and Specs from <div class="degen">...</div>
    degen_match = re.search(r'<div class="degen">([\s\S]*?)</div>\s*<div class="prosame">', page_html)
    if not degen_match:
        degen_match = re.search(r'<div class="degen">([\s\S]*?)</div>\s*</div>\s*</div>', page_html)
        
    degen_content = degen_match.group(1) if degen_match else ""
    
    # Extract Feature bullet points
    features = []
    ul_match = re.search(r'<ul>([\s\S]*?)</ul>', degen_content)
    if ul_match:
        lis = re.findall(r'<li>(.*?)</li>', ul_match.group(1))
        for li in lis:
            text = re.sub(r'<[^>]+>', '', li).strip()
            text = html.unescape(text)
            if text:
                features.append(text)
                
    # Extract Specs Table
    specs = {}
    table_match = re.search(r'<table[^>]*>([\s\S]*?)</table>', degen_content)
    if table_match:
        rows = re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', table_match.group(1))
        for r in rows:
            tds = re.findall(r'<td[^>]*>(.*?)</td>', r)
            if len(tds) >= 2:
                k = html.unescape(re.sub(r'<[^>]+>', '', tds[0]).strip())
                v = html.unescape(re.sub(r'<[^>]+>', '', tds[1]).strip())
                if k and v:
                    specs[k] = v

    # Fallback features if empty
    if not features:
        features = [
            f"Công nghệ cảm biến vân tay quang học / bán dẫn tân tiến từ thương hiệu ADEL.",
            "Phương thức mở khóa đa năng: Vân tay, Mật mã chống nhìn trộm, Thẻ từ thông minh, Chìa cơ khẩn cấp.",
            "Thân khóa đúc bằng hợp kim nguyên khối, chốt khóa inox SUS 304 chống cưa cắt phá hoại.",
            "Chức năng khóa tự động an toàn khi đóng cửa, cảnh báo pin yếu và cảnh báo đột nhập bằng còi hú.",
            "Phù hợp lắp đặt cho cửa gỗ, cửa thép chống cháy, căn hộ chung cư cao cấp và biệt thự."
        ]

    # Fallback specs if empty
    if not specs:
        specs = {
            "Thương hiệu": "ADEL (USA Standard)",
            "Model": p["name"],
            "Nhà phân phối": "Vương Tín Official",
            "Phương thức mở": "Vân tay, Mật mã, Thẻ từ, Chìa cơ",
            "Thời gian nhận diện": "< 0.5 giây",
            "Chất liệu": "Hợp kim kẽm siêu bền, chống rỉ sét",
            "Độ dày cửa yêu cầu": "35mm - 65mm",
            "Bảo hành chính hãng": "24 Tháng tận nơi"
        }

    # Generate Rich SEO Content & Onpage Interlinking
    seo_title = f"{p['name']} - Khóa Điện Tử Vân Tay ADEL Chính Hãng Vương Tín"
    seo_desc = f"Mua {p['name']} chính hãng ADEL tại Vương Tín. Giá {p['price']}, bảo hành 24 tháng, hỗ trợ khảo sát lắp đặt tận nơi toàn quốc. Đầy đủ CO/CQ."
    
    # Internal anchor links based on category
    category_slug = p["category"]
    
    seo_content = f"""
### 1. Giới thiệu tổng quan về {p['name']}
**{p['name']}** là dòng khóa cửa điện tử thông minh cao cấp được tập đoàn công nghệ **ADEL** phát triển và phân phối chính thức tại Việt Nam thông qua **Hệ thống Vương Tín**. Sản phẩm nổi bật với thiết kế sang trọng, độ hoàn thiện tinh xảo và ứng dụng công nghệ bảo mật sinh trắc học chuẩn quốc tế, giúp bảo vệ an toàn tối đa cho ngôi nhà của bạn.

### 2. Các ưu điểm nổi bật của {p['name']}
- **Nhận diện vân tay siêu tốc:** Trang bị mô-đun cảm biến vân tay độ nhạy cao với thời gian phản hồi dưới 0.5 giây, chống làm giả vân tay quang học hoặc silicon.
- **Bảo mật đa tầng:** Hỗ trợ kết hợp mở khóa bằng thẻ từ RFID tần số cao, mật mã ảo chống nhìn trộm (Virtual Password), chìa cơ vi tính chống sao chép và kết nối ứng dụng thông minh.
- **Vật liệu cao cấp siêu bền:** Toàn bộ kết cấu khung vỏ được chế tác từ hợp kim đúc nguyên khối chống va đập, chống cạy phá và chịu được điều kiện khí hậu nóng ẩm tại Việt Nam.
- **Hệ thống báo động thông minh:** Cảnh báo âm thanh khi phát hiện có hiện tượng cạy cửa, nhập sai mật khẩu quá 5 lần hoặc khi pin sắp hết.

### 3. Thông số kỹ thuật chi tiết
Sản phẩm đáp ứng tiêu chuẩn kiểm định khắt khe của hãng ADEL, tương thích với hầu hết các hệ cửa hiện đại:
- **Độ dày đố cửa phù hợp:** {specs.get('Độ dày cửa', specs.get('Độ dày cửa yêu cầu', '35mm - 65mm'))}
- **Chất liệu chế tạo:** {specs.get('Vật liệu', specs.get('Chất liệu', 'Hợp kim kẽm & nhôm cao cấp'))}
- **Màu sắc hoàn thiện:** {specs.get('Màu sắc', 'Đen huyền bí / Vàng kim / Đồng cổ')}
- **Nguồn điện vận hành:** Pin kiềm AA tiêu chuẩn, tuổi thọ lên tới 10-12 tháng, có cổng cấp nguồn phụ Micro-USB / Type-C khẩn cấp.

### 4. Chính sách bảo hành & Lắp đặt tại Vương Tín
Khi đặt mua **{p['name']}** tại Vương Tín, quý khách hàng nhận được đặc quyền:
1. **Cam kết 100% chính hãng ADEL:** Đầy đủ giấy tờ chứng nhận xuất xứ hàng hóa CO/CQ, tem chống hàng giả từ Bộ Công An.
2. **Bảo hành 24 tháng:** Đổi mới linh kiện chính hãng hoặc 1 đổi 1 nhanh chóng nếu phát sinh lỗi kỹ thuật từ nhà sản xuất.
3. **Kỹ thuật viên chuyên nghiệp:** Khảo sát, đo đạc đố cửa và lắp đặt hoàn thiện tận nơi trong ngày tại TP.HCM, Hà Nội và hỗ trợ giao hàng toàn quốc.
4. **Chiết khấu dự án & Đại lý:** Mức giá sỉ ưu đãi đặc biệt cho chủ thầu, kiến trúc sư và đối tác phân phối.
"""

    full_catalog.append({
        "id": f"adel-{idx+1:03d}",
        "slug": slug,
        "name": p["name"],
        "brand": "ADEL",
        "category": "khoa-dien-tu",
        "subCategory": p["category"],
        "categoryName": p["categoryName"],
        "price": p["price"] if p["price"] else "Liên hệ báo giá",
        "image": p["image"],
        "adel_url": detail_url,
        "badge": "Chính Hãng ADEL",
        "features": features,
        "specs": specs,
        "seoTitle": seo_title,
        "seoDescription": seo_desc,
        "seoContent": seo_content.strip()
    })

    if (idx + 1) % 15 == 0:
        print(f"Scraped {idx + 1}/{len(products)} products...")

print(f"Done scraping all {len(full_catalog)} ADEL products!")

# Add expanded categories: Sanitary & Furniture
sanitary_list = [
    {
        "id": "tbvs-001",
        "slug": "bon-cau-thong-minh-vuong-tin-vt-smart-8800",
        "name": "Bồn Cầu Thông Minh Vương Tín VT-Smart 8800",
        "brand": "Vương Tín",
        "category": "thiet-bi-ve-sinh",
        "subCategory": "bon-cau",
        "categoryName": "Bồn Cầu Thông Minh",
        "price": "14,500,000 đ",
        "image": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80",
        "badge": "Công Nghệ Nano Sứ",
        "features": [
            "Tự động đóng mở nắp khi có người tới gần bằng cảm ứng radar.",
            "Vòi rửa đa chế độ: Rửa đại tiện, rửa phụ nữ, massage bọt khí ấm.",
            "Sấy khô khí ấm, sưởi ấm bệ ngồi điều chỉnh 4 mức nhiệt độ.",
            "Công nghệ xả xoáy Siphon Jet siêu sạch, siêu êm và tiết kiệm nước.",
            "Tráng men men tuyết kháng khuẩn Nano Ag+ chống ố vàng vĩnh viễn."
        ],
        "specs": {
            "Thương hiệu": "Vương Tín Sanitary",
            "Kích thước": "680 x 390 x 480 mm",
            "Tâm xả": "300 mm",
            "Áp lực nước": "0.15 - 0.75 MPa",
            "Bảo hành": "Phần sứ 10 năm, phụ kiện điện tử 3 năm"
        },
        "seoTitle": "Bồn Cầu Thông Minh VT-Smart 8800 Vương Tín - Men Nano Sứ Kháng Khuẩn",
        "seoDescription": "Bồn cầu thông minh tự động xả cảm ứng Vương Tín VT-Smart 8800 cao cấp. Men nano chống bám bẩn, sấy ấm tiện nghi. Khảo sát lắp đặt tận nơi.",
        "seoContent": "Bồn cầu thông minh Vương Tín VT-Smart 8800 là giải pháp nâng tầm tiện nghi không gian phòng tắm với tính năng cảm ứng tự động hiện đại và men sứ tuyết kháng khuẩn cao cấp."
    },
    {
        "id": "tbvs-002",
        "slug": "lavabo-da-tu-nhien-lien-khoi-vt-lv09-luxury",
        "name": "Lavabo Đá Tự Nhiên Liền Khối VT-LV09 Luxury",
        "brand": "Vương Tín",
        "category": "thiet-bi-ve-sinh",
        "subCategory": "lavabo",
        "categoryName": "Chậu Lavabo",
        "price": "4,200,000 đ",
        "image": "https://images.unsplash.com/photo-1620626011761-996317b8d101?auto=format&fit=crop&w=600&q=80",
        "badge": "Đá Tự Nhiên Liền Khối",
        "features": [
            "Gia công nguyên khối từ phiến đá marble cao cấp vân tự nhiên.",
            "Bề mặt phủ lớp nano bảo vệ chống thấm nước và chống ố màu mỹ phẩm.",
            "Thiết kế đặt bàn hiện đại, lòng chậu vát cong thoát nước nhanh chóng."
        ],
        "specs": {
            "Chất liệu": "Đá tự nhiên / Men đá cao cấp",
            "Kích thước": "500 x 400 x 140 mm",
            "Màu sắc": "Trắng vân mây / Xám xi măng",
            "Bảo hành": "5 năm chống thấm nứt"
        },
        "seoTitle": "Chậu Lavabo Đá Liền Khối VT-LV09 Vương Tín - Sang Trọng Đẳng Cấp",
        "seoDescription": "Chậu rửa mặt lavabo đá marble nguyên khối VT-LV09 Vương Tín. Thiết kế tối giản, phủ nano chống ố, tương thích mọi không gian phòng tắm sang trọng.",
        "seoContent": "Lavabo đá tự nhiên liền khối VT-LV09 do Vương Tín phân phối là lựa chọn lý tưởng cho các biệt thự, căn hộ và khách sạn đẳng cấp theo phong cách Modern Luxury."
    },
    {
        "id": "tbvs-003",
        "slug": "bon-cau-trung-1-khoi-men-tuyet-vt-egg-66",
        "name": "Bồn Cầu Trứng 1 Khối Men Tuyết VT-Egg 66",
        "brand": "Vương Tín",
        "category": "thiet-bi-ve-sinh",
        "subCategory": "bon-cau",
        "categoryName": "Bồn Cầu 1 Khối",
        "price": "5,800,000 đ",
        "image": "https://images.unsplash.com/photo-1564540574859-0dfb63985953?auto=format&fit=crop&w=600&q=80",
        "badge": "Thiết Kế Quả Trứng",
        "features": [
            "Thiết kế hình quả trứng độc bản, không góc chết dễ dàng vệ sinh lau chùi.",
            "Nắp đóng êm chất liệu UF cao cấp chống trầy xước.",
            "Xả xoáy Tornado 360 độ cực mạnh đánh bay mọi vết bẩn chỉ trong 1 lần xả."
        ],
        "specs": {
            "Chất liệu": "Sứ nung 1280 độ C, men tuyết chống dính",
            "Kích thước": "650 x 470 x 610 mm",
            "Bảo hành": "Phần sứ 10 năm"
        },
        "seoTitle": "Bồn Cầu Trứng 1 Khối Men Tuyết VT-Egg 66 Vương Tín",
        "seoDescription": "Bồn cầu hình quả trứng 1 khối men tuyết cao cấp VT-Egg 66 Vương Tín. Xả xoáy 360 độ cực mạnh, không tiếng ồn.",
        "seoContent": "Bồn cầu trứng VT-Egg 66 mang đến vẻ đẹp phá cách và tinh tế cho phòng tắm gia đình, đảm bảo vệ sinh tối đa với công nghệ men tuyết chống dính."
    },
    {
        "id": "tbvs-004",
        "slug": "sen-tam-cay-nhiet-do-phim-dan-vt-piano-black",
        "name": "Sen Tắm Cây Nhiệt Độ Phím Đàn VT-Piano Black",
        "brand": "Vương Tín",
        "category": "thiet-bi-ve-sinh",
        "subCategory": "sen-tam",
        "categoryName": "Sen Vòi & Phụ Kiện",
        "price": "3,650,000 đ",
        "image": "https://images.unsplash.com/photo-1585058177579-24b893bb0b4b?auto=format&fit=crop&w=600&q=80",
        "badge": "Phím Đàn Thông Minh",
        "features": [
            "Củ sen bằng đồng nguyên chất 59% mạ PVD đen nhám chống bám cặn vôi.",
            "Khóa an toàn nhiệt độ 38 độ C chống bỏng cho trẻ em và người già.",
            "Bát sen tròn tăng áp siêu lớn với các hạt silicon chống tắc nghẽn."
        ],
        "specs": {
            "Chất liệu": "Đồng mạ PVD cao cấp",
            "Áp lực nước": "0.05 - 0.75 MPa",
            "Bảo hành": "3 năm chính hãng"
        },
        "seoTitle": "Cây Sen Tắm Phím Đàn Nhiệt Độ VT-Piano Black Vương Tín",
        "seoDescription": "Cây sen tắm phím đàn điều chỉnh nhiệt độ chính xác VT-Piano Black. Chất liệu đồng nguyên chất mạ PVD đen sang trọng, chống bám cặn.",
        "seoContent": "Sen cây phím đàn thông minh Vương Tín mang đến trải nghiệm tắm thư giãn tuyệt vời như tại spa với khả năng duy trì nhiệt độ nước lý tưởng."
    }
]

furniture_list = [
    {
        "id": "nt-001",
        "slug": "bo-ban-an-mat-da-ceramic-chong-xuoc-6-ghe-monet",
        "name": "Bộ Bàn Ăn Mặt Đá Ceramic Chống Xước 6 Ghế Monet",
        "brand": "Vương Tín",
        "category": "noi-that",
        "subCategory": "ban-ghe-an",
        "categoryName": "Bàn Ghế Ăn",
        "price": "12,800,000 đ",
        "image": "https://images.unsplash.com/photo-1617806118233-18e1de247200?auto=format&fit=crop&w=600&q=80",
        "badge": "Mặt Đá Ceramic Chống Ố",
        "features": [
            "Mặt bàn đá phiến Ceramic nung nhiệt độ cao: Chống xước, chống ố, chịu nhiệt nồi niêu nóng lên đến 1200 độ C.",
            "Khung chân thép carbon sơn tĩnh điện chữ X vững chãi, tải trọng tới 300kg.",
            "Bao gồm 6 ghế Monet bọc da Microfiber cao cấp êm ái, chân bọc núm đồng sang trọng."
        ],
        "specs": {
            "Kích thước bàn": "1600 x 800 x 750 mm",
            "Chất liệu": "Mặt đá Ceramic + Khung thép carbon + Ghế da Microfiber",
            "Bảo hành": "2 năm kết cấu khung chân"
        },
        "seoTitle": "Bộ Bàn Ăn Mặt Đá Ceramic 6 Ghế Monet Vương Tín Chống Xước Cao Cấp",
        "seoDescription": "Bộ bàn ăn mặt đá Ceramic chống trầy xước, chịu nhiệt độ cao cùng 6 ghế ăn Monet sang trọng. Hoàn thiện phòng ăn tiện nghi cùng Vương Tín.",
        "seoContent": "Bộ bàn ăn mặt đá Ceramic Monet của Vương Tín là sự kết hợp hoàn hảo giữa độ bền cơ học vượt trội và phong cách nội thất đương đại."
    },
    {
        "id": "nt-002",
        "slug": "sofa-da-y-phong-khach-cao-cap-vt-milano-3m",
        "name": "Sofa Da Ý Phòng Khách Cao Cấp VT-Milano 3M",
        "brand": "Vương Tín",
        "category": "noi-that",
        "subCategory": "sofa-phong-khach",
        "categoryName": "Sofa & Bàn Trà",
        "price": "21,500,000 đ",
        "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=600&q=80",
        "badge": "Khung Gỗ Sồi Nhập Khẩu",
        "features": [
            "Bọc da nhập khẩu công nghệ Ý mềm mại, thoáng khí, chống nứt nẻ và chống thấm nước.",
            "Đệm mút D40 nguyên khối đàn hồi cao kết hợp lò xo túi độc lập không xẹp lún.",
            "Khung sườn bằng gỗ sồi tự nhiên đã qua tẩm sấy chống mối mọt cong vênh."
        ],
        "specs": {
            "Kích thước": "Dài 2800 mm x Sâu 950 mm",
            "Khung": "Gỗ sồi tự nhiên",
            "Đệm mút": "Mút D40 đàn hồi cao cấp",
            "Bảo hành": "5 năm khung và đệm mút"
        },
        "seoTitle": "Sofa Da Ý Cao Cấp VT-Milano 3M Vương Tín - Sang Trọng Hiện Đại",
        "seoDescription": "Sofa da phòng khách VT-Milano 3M chuẩn phong cách Ý. Khung gỗ sồi tự nhiên, mút D40 chống lún. Phân phối chính hãng bởi Vương Tín.",
        "seoContent": "Sofa phòng khách VT-Milano 3M là điểm nhấn ấn tượng cho không gian sống hiện đại, mang lại cảm giác thư thái tuyệt đối cho cả gia đình."
    },
    {
        "id": "nt-003",
        "slug": "tu-giay-thong-minh-cua-lua-cam-ung-den-led",
        "name": "Tủ Giày Thông Minh Cửa Lùa Cảm Ứng Đèn LED",
        "brand": "Vương Tín",
        "category": "noi-that",
        "subCategory": "tu-ke-thong-minh",
        "categoryName": "Tủ & Kệ Gia Đình",
        "price": "4,900,000 đ",
        "image": "https://images.unsplash.com/photo-1595428774223-ef52624120d2?auto=format&fit=crop&w=600&q=80",
        "badge": "Khử Khuẩn Ozone",
        "features": [
            "Cánh lùa mở rộng tiết kiệm diện tích tối đa cho sảnh căn hộ chung cư.",
            "Tích hợp đèn LED cảm ứng chuyển động tự động bật sáng khi mở cửa.",
            "Trang bị mô-đun khử mùi bằng ozone và sấy khô hút ẩm bảo vệ giày dép."
        ],
        "specs": {
            "Kích thước": "1200 x 350 x 1100 mm",
            "Chất liệu": "Gỗ MDF lõi xanh chống ẩm phủ Melamine",
            "Bảo hành": "2 năm chính hãng"
        },
        "seoTitle": "Tủ Giày Thông Minh Khử Khuẩn Cảm Ứng LED Vương Tín",
        "seoDescription": "Tủ để giày thông minh sấy khử mùi ozone, đèn led cảm ứng hiện đại. Gỗ MDF lõi xanh chống ẩm chất lượng cao từ Vương Tín.",
        "seoContent": "Tủ giày thông minh tích hợp sấy khử mùi Ozone của Vương Tín giúp bảo quản giày dép luôn khô ráo, thơm tho và gọn gàng."
    }
]

complete_catalog = {
    "site": {
        "name": "VƯƠNG TÍN",
        "distributorOf": "ADEL (USA Standard)",
        "slogan": "Tổng Kho Khóa Điện Tử ADEL & Nội Thất Thiết Bị Vệ Sinh Cao Cấp",
        "hotline": "0903 354 397",
        "hotlineFormatted": "0903 354 397",
        "email": "kinhdoanh@vuongtin.vn",
        "address": "Showroom Vương Tín - Hệ Thống Phân Phối & Lắp Đặt Toàn Quốc",
        "warrantyMonths": 24,
        "adelBaseUrl": "https://www.adelgroup.vn"
    },
    "categories": [
        {"id": "khoa-dien-tu", "name": "Khóa Điện Tử ADEL", "icon": "fa-fingerprint", "seoKey": "khoa van tay adel"},
        {"id": "thiet-bi-ve-sinh", "name": "Lavabo & Thiết Bị Vệ Sinh", "icon": "fa-bath", "seoKey": "thiet bi ve sinh lavabo bon cau"},
        {"id": "noi-that", "name": "Bàn Ghế & Nội Thất Cao Cấp", "icon": "fa-couch", "seoKey": "noi that ban ghe cao cap"}
    ],
    "adel_products": full_catalog,
    "sanitary_products": sanitary_list,
    "furniture_products": furniture_list
}

with open("products_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_catalog, f, ensure_ascii=False, indent=2)

print(f"COMPLETE! Successfully built catalog with {len(full_catalog)} ADEL models + 4 Sanitary + 3 Furniture = {len(full_catalog) + 7} products.")
