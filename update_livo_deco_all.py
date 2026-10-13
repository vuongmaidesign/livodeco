import json
import os
import re
import glob

# 1. Clean up old HTML files in san-pham/ and tin-tuc/ that had vuong-tin or vt-
for old_f in glob.glob("san-pham/*.html") + glob.glob("tin-tuc/*.html"):
    if "vuong-tin" in old_f or "-vt-" in old_f:
        try:
            os.remove(old_f)
            print(f"Removed old file: {old_f}")
        except Exception as e:
            print(f"Error removing {old_f}: {e}")

# 2. Update build_news_policies.py and news_and_policies.json
with open("build_news_policies.py", "r", encoding="utf-8") as f:
    bnp_code = f.read()

bnp_code = bnp_code.replace("chinh-sach-dai-ly-nha-phan-phoi-khoa-adel-vuong-tin", "chinh-sach-dai-ly-nha-phan-phoi-khoa-adel-livo-deco")
bnp_code = bnp_code.replace("VƯƠNG TÍN", "LIVO DECO").replace("Vương Tín", "Livo Deco").replace("vuongtin.vn", "livodeco.vn").replace("vuong-tin", "livo-deco")

with open("build_news_policies.py", "w", encoding="utf-8") as f:
    f.write(bnp_code)

exec(compile(bnp_code, "build_news_policies.py", "exec"))

with open("news_and_policies.json", "r", encoding="utf-8") as f:
    news_policies_data = json.load(f)

# 3. Load and enrich products_data.json
with open("products_data.json", "r", encoding="utf-8") as f:
    pdata = json.load(f)

pdata["site"] = {
    "name": "LIVO DECO",
    "brandName": "Livo Deco",
    "domain": "https://livodeco.vn",
    "distributorOf": "ADEL (USA Standard - Since 1993)",
    "slogan": "Nhà Phân Phối Ủy Quyền Khóa Điện Tử ADEL & Nội Thất Thiết Bị Vệ Sinh Cao Cấp",
    "hotline": "0903 354 397",
    "hotlineFormatted": "0903 354 397",
    "email": "kinhdoanh@livodeco.vn",
    "address": "Showroom Livo Deco - Hệ Thống Phân Phối & Lắp Đặt Khóa ADEL Toàn Quốc (TP.HCM • Hà Nội • Đà Nẵng)",
    "warrantyMonths": 24,
    "adelBaseUrl": "https://www.adelgroup.vn"
}

pdata["news"] = news_policies_data["news"]
pdata["policies"] = news_policies_data["policies"]

all_lists = [
    pdata.get("adel_products", []),
    pdata.get("sanitary_products", []),
    pdata.get("furniture_products", [])
]

# First pass: update slugs and brand names
for prod_list in all_lists:
    for p in prod_list:
        p["slug"] = p["slug"].replace("vuong-tin", "livo-deco").replace("-vt-", "-ld-")
        p["name"] = p["name"].replace("Vương Tín", "Livo Deco").replace("VT-", "LD-")
        if p.get("brand") == "Vương Tín":
            p["brand"] = "Livo Deco"
        if "specs" in p:
            new_specs = {}
            for k, v in p["specs"].items():
                new_specs[k] = str(v).replace("Vương Tín", "Livo Deco").replace("VT-", "LD-")
            p["specs"] = new_specs

flat_products = pdata.get("adel_products", []) + pdata.get("sanitary_products", []) + pdata.get("furniture_products", [])

def build_rich_seo_geo_faq(p, all_prods):
    is_adel = p.get("category") == "khoa-dien-tu"
    cat_name = p.get("categoryName", "Khóa Điện Tử ADEL")
    sub_cat = p.get("subCategory", "khoa-van-tay")
    specs = p.get("specs", {})
    features = p.get("features", [])
    
    # Extract key specs for GEO & FAQ
    unlock_methods = specs.get("Mở khóa ", specs.get("Mở khóa", specs.get("Phương thức mở khóa", "Vân tay sinh trắc học, thẻ từ RFID, mật mã số và chìa cơ chống sao chép")))
    door_thickness = specs.get("Độ dày cửa", specs.get("Độ dày đố cửa", "Từ 35mm đến 75mm (đố cửa rộng >= 95mm cho cửa gỗ hoặc >= 55mm cho cửa nhôm hệ)"))
    material = specs.get("Vật liệu ", specs.get("Vật liệu", specs.get("Chất liệu", "Hợp kim kẽm/nhôm đúc nguyên khối siêu bền chống cạy phá, phủ bề mặt chống oxy hóa")))
    power_supply = specs.get("Nguồn điện", "4 viên pin kiềm AA 1.5V (tuổi thọ 10.000 lần đóng mở ~ 10-12 tháng), tích hợp cổng kích nguồn khẩn cấp")
    color = specs.get("Màu sắc ", specs.get("Màu sắc", "Đen nhám / Vàng kim / Bạc sang trọng"))
    capacity = specs.get("Dung lượng", "Lưu trữ 100 - 200 vân tay, 100 - 200 thẻ từ và mật mã chủ/khách")

    # Sibling products for On-page Internal Links
    siblings = [item for item in all_prods if item.get("subCategory") == sub_cat and item["id"] != p["id"]]
    if len(siblings) < 3:
        siblings = [item for item in all_prods if item.get("category") == p.get("category") and item["id"] != p["id"]]
    sib1 = siblings[0] if len(siblings) > 0 else p
    sib2 = siblings[1] if len(siblings) > 1 else p
    sib3 = siblings[2] if len(siblings) > 2 else p

    # SEO Title & Description
    if is_adel:
        p["seoTitle"] = f"{p['name']} Chính Hãng ADEL - Giá {p['price']} | Nhà Phân Phối Livo Deco"
        p["seoDescription"] = f"Mua {p['name']} chính hãng ADEL tại Livo Deco với giá niêm yết {p['price']}. Mở khóa: {unlock_methods}. Bảo hành 24 tháng, CO/CQ đầy đủ, khảo sát & lắp đặt tận nơi trong 2h tại TP.HCM, Hà Nội & toàn quốc."
    else:
        p["seoTitle"] = f"{p['name']} Cao Cấp Chính Hãng - Giá {p['price']} | Livo Deco"
        p["seoDescription"] = f"Đặt mua {p['name']} chính hãng thương hiệu Livo Deco. Giá ưu đãi {p['price']}, chất liệu {material}, bảo hành dài hạn, giao hàng và lắp đặt tận nơi toàn quốc."

    # GEO Key Takeaways (Generative Engine Optimization Summary)
    if is_adel:
        p["geoSummary"] = [
            f"Sản phẩm & Mã hiệu: {p['name']} (SKU: {p['id'].upper()}) thuộc phân khúc {cat_name}.",
            f"Thương hiệu & Phân phối: Hãng khóa thông minh ADEL (tiêu chuẩn Hoa Kỳ từ 1993) – Phân phối chính ngạch bởi Livo Deco (livodeco.vn).",
            f"Giá niêm yết chính hãng: {p['price']} (Bao gồm VAT/CO-CQ dự án, miễn phí khảo sát đố cửa tận nhà).",
            f"Phương thức mở khóa: {unlock_methods} – Nhận diện sinh trắc học siêu nhạy < 0.5 giây.",
            f"Vật liệu & Độ bền: {material}, chống cạy phá, thích nghi hoàn hảo khí hậu nóng ẩm Việt Nam.",
            f"Tương thích đố cửa: Độ dày cửa {door_thickness}; Phù hợp cho nhà phố, căn hộ chung cư, biệt thự và văn phòng.",
            f"Bảo hành & Hậu mãi: Bảo hành điện tử chính hãng 24 tháng, 1 đổi 1 trong 30 ngày, hỗ trợ kỹ thuật 24/7 qua Hotline 0903 354 397."
        ]
    else:
        p["geoSummary"] = [
            f"Sản phẩm & Mã hiệu: {p['name']} (SKU: {p['id'].upper()}) – Danh mục {cat_name}.",
            f"Đơn vị cung ứng: Hệ sinh thái Nội thất & Thiết bị vệ sinh cao cấp Livo Deco (livodeco.vn).",
            f"Giá niêm yết: {p['price']} – Cam kết hàng chuẩn loại 1, kiểm định chất lượng khắt khe.",
            f"Chất liệu cấu tạo: {material}, chống bám bẩn, dễ dàng vệ sinh và bền bỉ theo thời gian.",
            f"Dịch vụ đi kèm: Giao hàng tận nơi toàn quốc, lắp đặt hoàn thiện bởi đội ngũ kỹ thuật Livo Deco."
        ]

    # Local GEO data
    p["localGeo"] = {
        "south": "TP. Hồ Chí Minh (Quận 1, Quận 2 - Thảo Điền, Quận 3, Quận 7 - Phú Mỹ Hưng, TP. Thủ Đức, Bình Thạnh, Gò Vấp, Tân Bình, Phú Nhuận, Quận 10, Quận 12...), Bình Dương (Thuận An, Dĩ An, Thủ Dầu Một), Đồng Nai (Biên Hòa, Long Thành), Bà Rịa - Vũng Tàu, Long An, Cần Thơ.",
        "north_central": "Hà Nội (Cầu Giấy, Nam Từ Liêm, Tây Hồ, Hoàn Kiếm, Đống Đa, Thanh Xuân, Hà Đông, Long Biên, Gia Lâm...), Hải Phòng, Quảng Ninh, Đà Nẵng, Nha Trang, Nghệ An.",
        "sla": "Khảo sát đố cửa & lắp đặt tận nơi siêu tốc trong 2 giờ tại nội thành TP.HCM & Hà Nội; Giao hàng kèm hướng dẫn kỹ thuật 1-1 trên toàn quốc 63 tỉnh thành."
    }

    # FAQs (5 rich Q&As per product for FAQ Schema + On-page accordion)
    if is_adel:
        p["faqs"] = [
            {
                "q": f"1. {p['name']} lắp được cho loại cửa nào và kích thước đố cửa tối thiểu là bao nhiêu?",
                "a": f"Mẫu {p['name']} thuộc dòng {cat_name} của ADEL, tương thích tốt với các hệ cửa có độ dày {door_thickness}. Đối với cửa gỗ tự nhiên, cửa gỗ công nghiệp hoặc cửa thép chống cháy, đố cửa cần đạt độ rộng tối thiểu từ 95mm trở lên (hoặc từ 55mm đối với dòng khóa chuyên dụng cửa nhôm Xingfa). Kỹ thuật viên Livo Deco sẽ hỗ trợ khảo sát đo đạc đố cửa miễn phí tận nơi trước khi lắp đặt."
            },
            {
                "q": f"2. Khi {p['name']} hết pin hoặc quên mật khẩu thì mở cửa bằng cách nào?",
                "a": f"{p['name']} sử dụng nguồn {power_supply}. Trước khi hết pin khoảng 2-3 tuần, khóa sẽ phát âm thanh và đèn báo cảnh báo pin yếu mỗi khi mở cửa. Trong trường hợp hết sạch pin khi bạn vắng nhà lâu ngày, bạn có thể dùng chìa cơ khẩn cấp chống sao chép đi kèm theo bộ khóa, hoặc dùng sạc dự phòng cắm vào cổng kích nguồn khẩn cấp bên ngoài để mở khóa bình thường rồi thay pin mới."
            },
            {
                "q": f"3. Công nghệ bảo mật của {p['name']} có chống được cạy phá và nhìn trộm mật khẩu không?",
                "a": f"Hoàn toàn an toàn. Thân khóa {p['name']} được chế tạo từ {material} với hệ thống chốt khóa chống cắt cưa. Cảm biến vân tay sinh trắc học nhận diện đa điểm chỉ nhận vân tay sống (chống làm giả bằng silicon hay hình ảnh). Ngoài ra, tính năng Mã số ảo (Virtual Password) cho phép bạn bấm thêm các dãy số ngẫu nhiên trước hoặc sau mật khẩu thật để ngăn chặn tuyệt đối việc bị nhìn lén."
            },
            {
                "q": f"4. Mua {p['name']} tại Livo Deco được bảo hành bao lâu và quy trình lắp đặt như thế nào?",
                "a": f"Khi đặt mua {p['name']} tại Nhà phân phối Livo Deco (livodeco.vn), quý khách được hưởng chế độ bảo hành chính hãng 24 tháng tận nơi và đổi mới 1 đổi 1 trong 30 ngày đầu nếu có lỗi từ nhà sản xuất. Đội ngũ kỹ thuật Livo Deco sử dụng dưỡng khoét chuyên dụng đảm bảo thẩm mỹ 100% cho bộ cửa, có mặt lắp đặt chỉ sau 2 giờ tại TP.HCM và Hà Nội."
            },
            {
                "q": f"5. Livo Deco có cung cấp giấy tờ CO/CQ và chiết khấu cho dự án khi mua {p['name']} số lượng lớn không?",
                "a": f"Có. Livo Deco là đối tác phân phối ủy quyền chính thức thương hiệu ADEL tại Việt Nam. Chúng tôi cung cấp đầy đủ chứng nhận xuất xứ – chất lượng (CO/CQ), hóa đơn VAT điện tử và chính sách chiết khấu sỉ hấp dẫn dành cho chủ đầu tư, nhà thầu xây dựng, kiến trúc sư và đại lý trên toàn quốc."
            }
        ]
    else:
        p["faqs"] = [
            {
                "q": f"1. Sản phẩm {p['name']} tại Livo Deco có chất liệu và độ bền như thế nào?",
                "a": f"{p['name']} được Livo Deco tuyển chọn kỹ lưỡng với cấu tạo từ {material}, đảm bảo khả năng chịu lực, chống thấm ố và giữ vẻ đẹp sang trọng lâu dài trong điều kiện khí hậu nóng ẩm tại Việt Nam."
            },
            {
                "q": f"2. Chế độ bảo hành của {p['name']} tại hệ thống Livo Deco là bao lâu?",
                "a": f"Sản phẩm {p['name']} được bảo hành chính hãng dài hạn theo tiêu chuẩn của Livo Deco ({specs.get('Bảo hành', 'từ 2 đến 10 năm tùy hạng mục')}), hỗ trợ bảo trì tận nhà nhanh chóng qua Hotline 0903 354 397."
            },
            {
                "q": f"3. Livo Deco có hỗ trợ giao hàng và lắp đặt {p['name']} tận nơi không?",
                "a": f"Có. Livo Deco miễn phí vận chuyển nội thành và hỗ trợ giao hàng an toàn trên toàn quốc 63 tỉnh thành. Đội ngũ kỹ thuật viên giàu kinh nghiệm sẽ lắp đặt hoàn thiện và nghiệm thu trực tiếp tại công trình."
            },
            {
                "q": f"4. Tôi có thể mua {p['name']} trọn gói cùng khóa điện tử ADEL để nhận chiết khấu combo không?",
                "a": f"Chắc chắn được. Khi khách hàng mua kết hợp {p['name']} cùng các dòng khóa cửa thông minh ADEL tại Livo Deco sẽ nhận ngay gói ưu đãi chiết khấu Combo hoàn thiện nội thất từ 5% - 15%."
            }
        ]

    # Rich Markdown seoContent (used by index.html SPA view and static generator)
    feat_bullets = "\n".join([f"- **{f.strip()}**" for f in features[:6]]) if features else f"- **Mở khóa đa phương thức:** {unlock_methods}\n- **Chất liệu siêu bền:** {material}"
    
    p["seoContent"] = f"""### 1. Tổng quan thiết kế & Xuất xứ chính ngạch của {p['name']}
**{p['name']}** (Mã SKU: **{p['id'].upper()}**) là một trong những sản phẩm tiêu biểu thuộc dòng **{cat_name}**, hiện đang được nhập khẩu và phân phối ủy quyền chính thức tại Việt Nam bởi **Hệ thống Livo Deco (livodeco.vn)**. Với mức giá niêm yết **{p['price']}**, sản phẩm mang đến sự kết hợp hoàn hảo giữa ngôn ngữ thiết kế kiến trúc đương đại và tiêu chuẩn an ninh sinh trắc học khắt khe từ tập đoàn **ADEL (USA Standard – Since 1993)**.

Không chỉ đóng vai trò là thiết bị bảo vệ an ninh cửa ra vào, **{p['name']}** còn là điểm nhấn nội thất sang trọng, nâng tầm đẳng cấp cho căn hộ chung cư, biệt thự, nhà phố hiện đại cũng như các tòa nhà văn phòng và khách sạn 5 sao.

### 2. Phân tích công nghệ bảo mật & Ưu điểm kỹ thuật vượt trội
Được chế tạo từ **{material}** với tông màu **{color}**, **{p['name']}** sở hữu kết cấu nguyên khối vững chắc, chống lại các tác động ngoại lực, chống cạy phá và chống oxy hóa vượt trội trong điều kiện thời tiết nóng ẩm tại Việt Nam.
{feat_bullets}
- **Phương thức mở khóa linh hoạt:** {unlock_methods}.
- **Dung lượng bộ nhớ lớn:** {capacity}, dễ dàng thêm hoặc xóa từng người dùng trực tiếp trên khóa hoặc qua ứng dụng quản lý.
- **Vận hành ổn định, tiết kiệm năng lượng:** Sử dụng nguồn {power_supply}, có cảnh báo pin yếu sớm và cổng cấp nguồn dự phòng khẩn cấp.

### 3. Tiêu chuẩn đố cửa & Khả năng tương thích lắp đặt thực tế
Để đảm bảo độ khít tuyệt đối và tính thẩm mỹ cao nhất khi thi công, **{p['name']}** được thiết kế tối ưu cho các hệ cửa có thông số:
- **Độ dày đố cửa yêu cầu:** {door_thickness}.
- **Loại cửa tương thích:** Cửa gỗ tự nhiên (gỗ lim, căm xe, gõ đỏ, sồi), cửa gỗ công nghiệp chống ẩm (MDF, HDF, Composite), cửa thép chống cháy chung cư hoặc cửa nhôm kính Xingfa (tùy theo hệ cơ khóa).
- **Quy trình thi công chuẩn hãng:** Đội ngũ kỹ sư **Livo Deco** sử dụng bộ khuôn dưỡng khoét lỗ khóa chuyên dụng của ADEL, cam kết không làm nứt vỡ kết cấu gỗ hay biến dạng khung cửa.

### 4. Quyền lợi bảo hành 24 tháng & Cam kết từ Nhà Phân Phối Livo Deco
Khi lựa chọn **{p['name']}** tại **Livo Deco**, quý khách hàng và đối tác dự án hoàn toàn yên tâm với cam kết dịch vụ 5 sao:
- **Hàng chính hãng 100% có đầy đủ CO/CQ:** Cung cấp trọn bộ hồ sơ chứng nhận xuất xứ, chất lượng và hóa đơn VAT phục vụ nghiệm thu công trình, dự án.
- **Bảo hành điện tử 24 tháng tận nơi:** Đổi mới 1 đổi 1 trong 30 ngày đầu nếu phát sinh lỗi kỹ thuật từ nhà sản xuất; bảo trì trọn đời sản phẩm.
- **Khảo sát & Lắp đặt siêu tốc trong 2 giờ:** Hỗ trợ khảo sát đố cửa miễn phí tại TP.HCM, Hà Nội, Đà Nẵng, Bình Dương, Đồng Nai và giao hàng toàn quốc.
- **Tham khảo thêm các dòng sản phẩm liên quan tại Livo Deco:** Quý khách có thể xem thêm [{sib1['name']}](san-pham/{sib1['slug']}.html) ({sib1['price']}), [{sib2['name']}](san-pham/{sib2['slug']}.html) ({sib2['price']}) hoặc [{sib3['name']}](san-pham/{sib3['slug']}.html) ({sib3['price']}) để chọn được model ưng ý nhất."""

for prod_list in all_lists:
    for p in prod_list:
        build_rich_seo_geo_faq(p, flat_products)

with open("products_data.json", "w", encoding="utf-8") as f:
    json.dump(pdata, f, ensure_ascii=False, indent=2)

# Write data.js with both LIVODECO_DATA and VUONGTIN_DATA alias
with open("data.js", "w", encoding="utf-8") as f:
    json_str = json.dumps(pdata, ensure_ascii=False)
    f.write(f"window.LIVODECO_DATA = {json_str};\nwindow.VUONGTIN_DATA = window.LIVODECO_DATA;\n")

print(f"Successfully updated products_data.json and data.js for {len(flat_products)} products with Livo Deco brand, SEO, GEO, and FAQs!")
