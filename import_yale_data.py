import json
import os

with open("products_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Update site info to reflect Yale partnership
data["site"]["distributorOf"] = "ADEL & YALE (Assa Abloy) - USA Standards"
data["site"]["slogan"] = "Nhà Phân Phối Ủy Quyền Khóa Điện Tử ADEL, YALE & Nội Thất Thiết Bị Vệ Sinh Cao Cấp"

# Check if Yale category exists, if not add it
cat_ids = [c["id"] for c in data.get("categories", [])]
if "khoa-dien-tu-yale" not in cat_ids:
    data["categories"].insert(1, {
        "id": "khoa-dien-tu-yale",
        "name": "Khóa Thông Minh YALE",
        "icon": "fa-shield-halved",
        "seoKey": "khoa thong minh yale assa abloy chinh hang"
    })

yale_products = [
    {
        "id": "yale-001",
        "slug": "khoa-dien-tu-yale-luna-pro",
        "name": "Khóa điện tử Yale Luna Pro Push-Pull Cao Cấp",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-push-pull",
        "categoryName": "Khóa Push-Pull Thông Minh YALE",
        "price": "18,500,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-luna-pro.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 18",
        "badge": "Flagship YALE 2025",
        "features": [
            "Công nghệ quét vân tay Liveness 3 trong 1 (SenseTM Pixel + Live Finger Detection + Heart Rate nhịp tim sống)",
            "Mở khóa đa phương thức: Vân tay Liveness, Thẻ từ CPU bảo mật cao, Mã số PIN, App Yale Access / Yale Home, Chìa cơ",
            "Màn hình thông báo trạng thái hoạt động trực quan & Hướng dẫn bằng giọng nói đa ngôn ngữ",
            "Khóa tự động hoàn toàn (Full Auto Mortice) – Tự động thu và phóng chốt khi đóng cửa",
            "Hệ thống báo động đột nhập & cạy phá khóa âm lượng lớn 80dB",
            "Mã PIN giả (Fake PIN code) chống nhìn trộm và dò dấu vân tay trên màn hình cảm ứng",
            "Cảnh báo pin yếu bằng âm thanh và đèn LED báo hiệu trước 2-3 tuần",
            "Cổng cấp nguồn khẩn cấp USB-C tiện lợi khi khóa cạn pin",
            "Tùy chọn kết nối mở rộng: Bluetooth Module, Yale Connect Plus Hub 2 - Wifi, Zigbee & Z-Wave 700"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa điện tử thông minh Push-Pull Yale Luna Pro",
            "Mã hiệu": "LunaP-IG17-5B-35-NN-001 (BS 60mm) / LunaP-IG17-5B-35-NN-000 (BS 70mm)",
            "Thương hiệu": "YALE (Tập đoàn ASSA ABLOY - Hoa Kỳ từ 1840)",
            "Phương thức mở khóa": "Vân tay Liveness 3-in-1, Thẻ CPU mã hóa, Mã số ảo, App điện thoại, Chìa cơ khẩn cấp",
            "Dung lượng bộ nhớ": "Tối đa 100 vân tay, 100 thẻ từ CPU, 100 mã số người dùng",
            "Kích thước mặt ngoài": "103 mm (Rộng) x 424 mm (Cao) x 49 mm (Sâu)",
            "Kích thước mặt trong": "76 mm (Rộng) x 420 mm (Cao) x 62.7 mm (Sâu)",
            "Khoảng cách từ cạnh cửa (Backset)": "60 mm & 70 mm (Tùy chọn thân khóa theo đố cửa)",
            "Độ dày cửa phù hợp": "35 mm ~ 100 mm (Cửa gỗ tự nhiên, cửa thép chống cháy, cửa composite cao cấp)",
            "Màu sắc hoàn thiện": "Vàng Champagne Gold / Đen mờ sang trọng",
            "Chất liệu chế tác": "Hợp kim kẽm & nhôm đúc nguyên khối chống va đập, phủ sơn tĩnh điện nano chống bám vân tay",
            "Nguồn điện hoạt động": "4 viên Pin kiềm Alkaline AA 1.5V (Tuổi thọ ~10.000 lần đóng mở)",
            "Nguồn cấp khẩn cấp": "Cổng USB-C 5V thông dụng",
            "Âm lượng còi báo động": "80dB cảnh báo cạy cửa, chống cháy và đột nhập trái phép",
            "Bảo hành chính hãng": "24 tháng tận nơi tại Livo Deco - Đổi mới 1 đổi 1 trong 30 ngày"
        },
        "seoTitle": "Khóa Điện Tử Yale Luna Pro Push-Pull Chính Hãng 2025 | Livo Deco",
        "seoDescription": "Mua Khóa điện tử Yale Luna Pro Push-Pull chính hãng ASSA ABLOY tại Livo Deco giá 18.500.000 đ. Vân tay Liveness 3 trong 1 nhịp tim, thẻ CPU, app Yale Home, bảo hành 24T tận nơi.",
        "seoContent": "### 1. Tổng quan thiết kế & Đẳng cấp Flagship của Yale Luna Pro\n**Yale Luna Pro** là tuyệt tác khóa điện tử thông minh dạng Push-Pull thế hệ mới nhất thuộc danh mục **YALE CATALOGUE 2025**, được phát triển bởi **tập đoàn ASSA ABLOY (Thương hiệu khóa Yale lừng danh Hoa Kỳ từ năm 1840)**. Tại thị trường Việt Nam, **Livo Deco (livodeco.vn)** là đối tác phân phối ủy quyền chính hãng, mang đến sản phẩm khóa cửa cao cấp nhất cho các biệt thự, penthouse và căn hộ hạng sang.\n\nThiết kế tay nắm kéo đẩy công thái học (Ergonomic Push-Pull) của **Yale Luna Pro** giúp thao tác mở cửa trở nên êm ái chỉ với một chạm đẩy nhẹ hoặc kéo nhẹ, biến không gian sảnh chính ngôi nhà trở nên tiện nghi và đẳng cấp vượt bậc.\n\n### 2. Đột phá công nghệ bảo mật vân tay Liveness 3 trong 1\nĐiểm khác biệt đưa **Yale Luna Pro** dẫn đầu phân khúc khóa cửa thông minh cao cấp chính là giải pháp quét vân tay **Liveness 3 trong 1** độc quyền của Yale:\n- **SenseTM Pixel:** Cảm biến quang học siêu phân giải ghi nhận cấu trúc rãnh vân tay đến từng micromet.\n- **Live Finger Detection:** Nhận diện tế bào biểu bì sống, chống lại mọi loại vân tay giả làm từ silicon, cao su, gelatin hay ảnh chụp 3D.\n- **Heart Rate Detection:** Cảm biến sinh trắc học nhịp tim và tuần hoàn mao mạch dưới da, đảm bảo chỉ có ngón tay của người sống đang thao tác mới được phép mở cửa.\n- **Bảo mật thẻ từ CPU & Mã PIN ảo:** Thẻ CPU chống sao chép công nghệ thẻ ngân hàng cùng chức năng Fake PIN code bảo vệ tuyệt đối mật khẩu thật trước ánh nhìn của người lạ.\n- **Kết nối thông minh Yale Home Cloud:** Cho phép gia chủ theo dõi lịch sử ra vào, cấp mã số khách tạm thời từ xa qua điện thoại thông minh.\n\n### 3. Tiêu chuẩn đố cửa & Quy chuẩn thi công của Livo Deco\n**Yale Luna Pro** được thiết kế nguyên khối chắc chắn, tương thích hoàn hảo với các hệ cửa:\n- **Độ dày cánh cửa yêu cầu:** 35mm đến 100mm.\n- **Đố cửa:** Đạt chiều rộng từ 105mm trở lên (tương thích cả 2 chuẩn Backset 60mm và 70mm).\n- **Chất liệu cửa:** Cửa gỗ tự nhiên (gõ đỏ, óc chó, sồi, lim), cửa gỗ công nghiệp cao cấp, cửa thép chống cháy tại các khu đô thị lớn như Vinhomes, Novaland, Ecopark, Phú Mỹ Hưng.\n- **Quy trình lắp đặt:** Đội ngũ kỹ sư Livo Deco sử dụng bộ dưỡng lấy dấu chuẩn của ASSA ABLOY, thi công không bụi bẩn, không trầy xước bề mặt cửa trong vòng 2 giờ.\n\n### 4. Chính sách bảo hành 24 tháng & Phân phối chính hãng từ Livo Deco\nKhách hàng mua **Yale Luna Pro** tại Livo Deco được bảo đảm tuyệt đối về xuất xứ và quyền lợi:\n- Đầy đủ chứng từ nhập khẩu chính ngạch CO/CQ từ tập đoàn ASSA ABLOY Việt Nam, cung cấp hóa đơn VAT dự án.\n- Bảo hành điện tử chính hãng 24 tháng tận nơi, đổi mới 1 đổi 1 trong 30 ngày đầu tiên nếu phát sinh sự cố kỹ thuật.\n- Miễn phí khảo sát đố cửa và giao hàng lắp đặt tận nhà tại TP. Hồ Chí Minh, Hà Nội, Đà Nẵng và các tỉnh lân cận.",
        "infographics": [],
        "geoSummary": [
            "Sản phẩm: Khóa điện tử Push-Pull Yale Luna Pro (YALE CATALOGUE 2025).",
            "Thương hiệu: YALE (ASSA ABLOY Group - USA) – Phân phối chính thức bởi Livo Deco.",
            "Giá niêm yết: 18,500,000 đ (Miễn phí khảo sát & lắp đặt tận nơi, bảo hành 24 tháng).",
            "Công nghệ cốt lõi: Vân tay Liveness 3-in-1 (Pixel + Live Finger + Heart Rate), Thẻ CPU, App Yale Home.",
            "Kích thước mặt ngoài: 103 x 424 x 49 mm | Mặt trong: 76 x 420 x 62.7 mm | Backset 60/70mm.",
            "Tương thích cửa: Cửa gỗ tự nhiên, cửa thép chung cư, đố dày 35-100mm.",
            "Phạm vi phục vụ: Showroom & kỹ thuật viên lắp đặt tại TP.HCM, Hà Nội, Đà Nẵng và 63 tỉnh thành."
        ],
        "localGeo": {
            "south": "Showroom Livo Deco TP.HCM phục vụ Quận 1, Quận 2 (Thảo Điền, An Phú), Quận 7 (Phú Mỹ Hưng), TP. Thủ Đức, Bình Thạnh, Bình Dương, Đồng Nai, Vũng Tàu.",
            "north_central": "Khu vực Hà Nội (Tây Hồ, Cầu Giấy, Hoàn Kiếm, Nam Từ Liêm, Long Biên, Ecopark, Ocean Park), Hải Phòng, Quảng Ninh, Đà Nẵng.",
            "sla": "Kỹ thuật viên Livo Deco có mặt khảo sát và hoàn thiện lắp đặt khóa Yale Luna Pro trong 2 giờ tại nội thành."
        },
        "faqs": [
            {
                "q": "1. Khóa Yale Luna Pro sử dụng công nghệ vân tay Liveness 3 trong 1 là gì?",
                "a": "Liveness 3 trong 1 là công nghệ bảo mật độc quyền của Yale tích hợp 3 lớp xác thực đồng thời: SenseTM Pixel quét ảnh vân tay độ nét cao, Live Finger Detection nhận diện mô da sống và Heart Rate Detection phát hiện nhịp đập mao mạch. Công nghệ này loại bỏ 100% nguy cơ làm giả vân tay bằng silicon hay khuôn đúc tinh vi."
            },
            {
                "q": "2. Cửa chung cư hoặc cửa biệt thự đố dày bao nhiêu thì lắp vừa khóa Yale Luna Pro?",
                "a": "Khóa điện tử Yale Luna Pro tương thích với độ dày cánh cửa từ 35mm đến 100mm. Độ rộng đố cửa tối thiểu cần đạt từ 105mm trở lên để chứa vừa thân khóa Backset 60mm hoặc 70mm. Đội ngũ Livo Deco luôn hỗ trợ đo đạc và tư vấn trực tiếp miễn phí trước khi quý khách đưa ra quyết định."
            },
            {
                "q": "3. Khi khóa Yale Luna Pro hết pin thì phải mở cửa bằng cách nào?",
                "a": "Yale Luna Pro có cảnh báo pin yếu trước 2-3 tuần qua màn hình và âm thanh mỗi lần đóng mở. Nếu vắng nhà dài ngày khiến pin cạn kiệt, bạn có thể cắm sạc dự phòng qua cổng USB-C đặt ẩn dưới đáy khóa để kích nguồn khẩn cấp tức thì, hoặc dùng chìa cơ bảo mật cao đi kèm."
            },
            {
                "q": "4. Chế độ bảo hành và nguồn gốc xuất xứ của Yale Luna Pro tại Livo Deco ra sao?",
                "a": "Sản phẩm Yale Luna Pro phân phối tại Livo Deco là hàng chính ngạch 100% từ ASSA ABLOY Việt Nam, có đầy đủ chứng chỉ CO/CQ và hóa đơn VAT. Khóa được bảo hành chính hãng 24 tháng tại nhà, 1 đổi 1 trong 30 ngày và hỗ trợ kỹ thuật bảo trì trọn đời."
            }
        ]
    },
    {
        "id": "yale-002",
        "slug": "khoa-dien-tu-yale-kyra-pro",
        "name": "Khóa điện tử Yale Kyra Pro Push-Pull Hiện Đại",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-push-pull",
        "categoryName": "Khóa Push-Pull Thông Minh YALE",
        "price": "14,800,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-kyra-pro.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 19",
        "badge": "Hot Trend YALE 2025",
        "features": [
            "Thiết kế Push-Pull phong cách tối giản thanh lịch với 2 tông màu Black (Đen mờ) và Champagne Gold (Vàng kim)",
            "Cảm biến vân tay Liveness 3 trong 1 tiên tiến (SenseTM Pixel + Live Finger Detection + Heart Rate nhịp tim)",
            "Đa dạng cách mở cửa: Vân tay, Thẻ từ RFID, Mã số ảo PIN Code, Chìa cơ, Tùy chọn Module Bluetooth & Wifi",
            "Màn hình thông báo trạng thái hoạt động bằng các ký hiệu số trực quan",
            "Hướng dẫn cài đặt và sử dụng bằng giọng nói thông minh (Voice guide feature)",
            "Chế độ khóa cửa tự động hoàn toàn Automatic Locking",
            "Chuông báo động 80dB khi phát hiện cạy phá hoặc số lần nhập sai liên tiếp",
            "Cấp nguồn khẩn cấp bằng pin 9V thông dụng khi khóa cạn pin"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa điện tử kéo đẩy Yale Kyra Pro",
            "Mã hiệu": "KyraP-IB03-6B-35-NN-001 (Màu đen 60mm) / KyraP-IG17-6B-35-NN-001 (Màu vàng 60mm)",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Phương thức mở khóa": "Vân tay Liveness 3-in-1, Mã số ảo, Thẻ từ RFID, Chìa cơ, Tùy chọn Bluetooth/Wifi",
            "Dung lượng bộ nhớ": "100 vân tay, 100 thẻ từ RFID, 100 mã số",
            "Kích thước mặt ngoài": "78 mm (Rộng) x 390 mm (Cao) x 50 mm (Sâu)",
            "Kích thước mặt trong": "76 mm (Rộng) x 390 mm (Cao) x 60 mm (Sâu)",
            "Backset": "60 mm & 70 mm",
            "Độ dày cửa phù hợp": "40 mm ~ 100 mm",
            "Màu sắc": "Black (Đen tuyền cá tính) / Champagne Gold (Vàng kim sang trọng)",
            "Nguồn điện": "4 viên Pin AA 1.5V, hỗ trợ kích nguồn ngoài qua chấu pin 9V",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Khóa Điện Tử Yale Kyra Pro Push-Pull Chính Hãng 2025 | Livo Deco",
        "seoDescription": "Khóa điện tử Yale Kyra Pro Push-Pull chính hãng giá 14.800.000 đ tại Livo Deco. Vân tay Liveness 3 trong 1, mã số ảo, thẻ từ RFID, đố cửa 40-100mm, bảo hành 24T toàn quốc.",
        "seoContent": "### 1. Đột phá phong cách kiến trúc với khóa Push-Pull Yale Kyra Pro\n**Yale Kyra Pro** mang đến làn gió mới cho không gian sống hiện đại với dáng dấp thanh mảnh, đường cong bo tròn tinh tế và bảng màu sang trọng (Black tuyền & Gold ánh kim). Sản phẩm nằm trong bộ sưu tập chủ lực của **YALE CATALOGUE 2025**, được người tiêu dùng đánh giá cao nhờ sự tiện dụng của tay cầm đẩy - kéo thế hệ mới.\n\n### 2. An toàn tuyệt đối với cảm biến vân tay sinh trắc học sống\nTrang bị bộ vi xử lý và cảm biến **Liveness 3 trong 1**, Yale Kyra Pro phân tích chiều sâu rãnh vân, độ đàn hồi của da sống và xung nhịp tim người thao tác. Thời gian mở khóa chỉ 0.3 giây, cực kỳ nhạy bén kể cả với ngón tay người già hay trẻ nhỏ.\n\n### 3. Tương thích đố cửa & Lắp đặt tiêu chuẩn\nKhóa tương thích với các loại cửa gỗ, cửa thép có độ dày từ 40mm đến 100mm. Livo Deco hỗ trợ khảo sát và cung cấp dịch vụ lắp đặt tận nơi tại TP.HCM, Hà Nội và Đà Nẵng.\n\n### 4. Cam kết bảo hành chính hãng Livo Deco\nSản phẩm được bảo hành chính hãng 24 tháng theo tiêu chuẩn của ASSA ABLOY Việt Nam, hỗ trợ kỹ thuật và đổi mới 1 đổi 1 trong 30 ngày nếu phát sinh lỗi nhà sản xuất.",
        "infographics": [],
        "geoSummary": [
            "Model: Khóa điện tử Yale Kyra Pro (Push-Pull 2025).",
            "Thương hiệu: YALE (ASSA ABLOY Hoa Kỳ) – Phân phối bởi Livo Deco.",
            "Giá niêm yết: 14,800,000 đ.",
            "Tính năng: Vân tay Liveness 3-in-1, thẻ từ, mã số ảo, báo động 80dB, khóa tự động.",
            "Kích thước: 78 x 390 x 50 mm (Mặt ngoài), Backset 60/70mm, Cửa dày 40-100mm."
        ],
        "localGeo": {
            "south": "TP.HCM (Quận 1, 2, 7, Thủ Đức, Bình Thạnh, Tân Bình...), Bình Dương, Đồng Nai.",
            "north_central": "Hà Nội (Cầu Giấy, Tây Hồ, Thanh Xuân, Nam Từ Liêm...), Đà Nẵng, Hải Phòng.",
            "sla": "Lắp đặt tiêu chuẩn hoàn thiện trong 2 giờ tại nội thành."
        },
        "faqs": [
            {
                "q": "1. Khóa Yale Kyra Pro khác gì so với dòng khóa tay gạt truyền thống?",
                "a": "Yale Kyra Pro sử dụng cơ chế kéo đẩy Push-Pull tiện dụng: khi đi chợ xách nhiều đồ đạc, bạn chỉ cần dùng cùi chỏ hoặc mu bàn tay đẩy nhẹ là cửa tự động mở mà không cần nắm xoay tay gạt như khóa truyền thống."
            },
            {
                "q": "2. Khóa Yale Kyra Pro có kết nối mở cửa bằng điện thoại được không?",
                "a": "Có. Khóa tích hợp khe cắm mở rộng cho Module Bluetooth Yale Home hoặc Hub Wifi Yale Connect Plus, cho phép bạn mở khóa từ xa và kiểm soát lịch sử ra vào qua điện thoại thông minh."
            }
        ]
    },
    {
        "id": "yale-003",
        "slug": "khoa-dien-tu-yale-ydm7116a",
        "name": "Khóa điện tử Yale YDM7116A Tay Gạt Đa Năng",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-tay-gat",
        "categoryName": "Khóa Vân Tay Tay Gạt YALE",
        "price": "11,200,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-ydm7116a.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 20",
        "badge": "Huyền Thoại YALE",
        "features": [
            "Mẫu khóa tay gạt kinh điển bán chạy nhất thế giới của thương hiệu Yale Assa Abloy",
            "Cảm biến vân tay Liveness 3 trong 1 chống làm giả đỉnh cao (Live Finger + Heart Rate + SenseTM Pixel)",
            "Phương thức mở khóa: Vân tay (100), Thẻ từ RFID (100), Mã số ảo (100), Chìa cơ vi tính (2 chìa), Bluetooth/Wifi",
            "3 tùy chọn màu sắc sang trọng: Red Bronze (Đồng đỏ quý phái), Champagne Gold (Vàng kim), Matt Black (Đen mờ)",
            "Chức năng mã số ảo Fake PIN code chống lộ mật khẩu",
            "Khóa tự động và báo động cạy cửa, báo cháy âm lượng 80dB",
            "Cảnh báo pin yếu bằng âm thanh và đèn LED, hỗ trợ chấu pin 9V khẩn cấp"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa điện tử vân tay tay gạt Yale YDM7116A",
            "Mã hiệu": "YDM7116A MB (Đen) / YDM7116A CG (Vàng) / YDM7116A RB (Đồng đỏ)",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Phương thức mở khóa": "Vân tay sinh trắc học, Thẻ từ RFID, Mã số, Chìa cơ, Tùy chọn Bluetooth/Wifi",
            "Dung lượng bộ nhớ": "Tối đa 100 vân tay, 100 thẻ từ, 100 mã số",
            "Kích thước mặt ngoài": "68 mm (Rộng) x 340 mm (Cao) x 40.18 mm (Sâu)",
            "Kích thước mặt trong": "72 mm (Rộng) x 344 mm (Cao) x 36 mm (Sâu)",
            "Khoảng cách tâm khóa (Backset)": "60 mm (Mặc định) hoặc 70 mm",
            "Độ dày cửa phù hợp": "40 mm ~ 90 mm",
            "Chất liệu": "Hợp kim kẽm đúc nguyên khối siêu cứng chống ăn mòn",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Khóa Vân Tay Yale YDM7116A Chính Hãng Giá Tốt Nhất | Livo Deco",
        "seoDescription": "Khóa điện tử vân tay Yale YDM7116A chính hãng giá 11.200.000 đ tại Livo Deco. Công nghệ Liveness 3-in-1, thẻ từ, mã PIN ảo, 3 màu sắc cao cấp, bảo hành 24T tận nhà.",
        "seoContent": "### 1. Huyền thoại khóa điện tử tay gạt Yale YDM7116A\nĐược vinh danh là một trong những mẫu khóa tay gạt bền bỉ và ổn định nhất của tập đoàn **ASSA ABLOY**, **Yale YDM7116A** đã hiện diện tại hàng triệu căn hộ và dự án cao cấp trên toàn cầu. Thiết kế tay gạt truyền thống vừa tay, kết hợp các góc cạnh bo viền mềm mại tạo nên vẻ đẹp vượt thời gian.\n\n### 2. Bộ ba màu sắc hoàn thiện đẳng cấp\nYale YDM7116A mang đến 3 phong cách hoàn thiện phù hợp mọi tông cửa gỗ và nội thất:\n- **Đồng đỏ (Red Bronze):** Đậm chất tân cổ điển quý tộc cho cửa gỗ lim, gõ đỏ.\n- **Vàng Champagne (Champagne Gold):** Quyến rũ, sang trọng cho phong cách hiện đại Luxury.\n- **Đen mờ (Matt Black):** Tối giản, thanh lịch, chuẩn mực căn hộ cao cấp.\n\n### 3. Công nghệ quét vân tay Liveness 3 trong 1\nTích hợp cảm biến vân tay quang học sinh trắc học đỉnh cao nhận diện nhịp tim mao mạch, đảm bảo sự an tâm tuyệt đối cho gia đình bạn.",
        "infographics": [],
        "geoSummary": [
            "Model: Khóa điện tử tay gạt Yale YDM7116A.",
            "Thương hiệu: YALE (ASSA ABLOY) – Phân phối bởi Livo Deco.",
            "Giá niêm yết: 11,200,000 đ (Bảo hành 24 tháng tận nơi).",
            "Kích thước: 68 x 340 x 40.18 mm | Cửa dày 40-90mm | Backset 60/70mm."
        ],
        "localGeo": {
            "south": "TP.HCM (Quận 1, 3, 7, Bình Thạnh, TP. Thủ Đức...), Bình Dương, Đồng Nai.",
            "north_central": "Hà Nội (Hoàn Kiếm, Ba Đình, Cầu Giấy, Tây Hồ...), Đà Nẵng.",
            "sla": "Lắp đặt thần tốc trong 2 giờ tại nội thành."
        },
        "faqs": [
            {
                "q": "1. Khóa Yale YDM7116A có phù hợp lắp cho cửa chung cư cửa gỗ không?",
                "a": "Rất phù hợp. Yale YDM7116A là dòng khóa tiêu chuẩn cho cửa gỗ tự nhiên và cửa thép chống cháy chung cư với độ dày từ 40mm đến 90mm và đố cửa rộng từ 95mm trở lên."
            }
        ]
    },
    {
        "id": "yale-004",
        "slug": "khoa-dien-tu-yale-ydm4109a",
        "name": "Khóa điện tử Yale YDM4109A Quét Vân Tay Sinh Trắc Học",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-tay-gat",
        "categoryName": "Khóa Vân Tay Tay Gạt YALE",
        "price": "9,800,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-ydm4109a.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 21",
        "badge": "Bán Chạy Nhất YALE",
        "features": [
            "Thế hệ nâng cấp của dòng khóa vân tay YDM4109 danh tiếng của Yale toàn cầu",
            "Cảm biến vân tay Liveness 3 trong 1 (SenseTM Pixel + Live Finger + Heart rate)",
            "Nắp trượt bảo vệ mắt đọc vân tay tự động đóng mở, chống bụi và chống nước",
            "Bàn phím cảm ứng ẩn sang trọng với công nghệ mã số ảo chống nhìn trộm",
            "Mở khóa: Vân tay (100), Mã số (100), Chìa cơ, Tùy chọn Bluetooth & Wifi",
            "3 màu sắc: Black (Đen), Gold (Vàng), Silver (Bạc)",
            "Báo động 80dB khi bị cạy phá hoặc nhập sai mật khẩu",
            "Cửa dày 40 - 80mm, Backset 60mm & 70mm"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa điện tử vân tay tay gạt Yale YDM4109A",
            "Mã hiệu": "YDM4109A BLK (Đen) / YDM4109A GOLD (Vàng) / YDM4109A SIL (Bạc)",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Phương thức mở khóa": "Vân tay Liveness, Mã số ảo, Chìa cơ, Tùy chọn Bluetooth",
            "Dung lượng bộ nhớ": "100 vân tay, 100 mã số",
            "Kích thước mặt ngoài": "68.6 mm (Rộng) x 320.7 mm (Cao) x 40.1 mm (Sâu)",
            "Kích thước mặt trong": "72.8 mm (Rộng) x 306.6 mm (Cao) x 37 mm (Sâu)",
            "Độ dày cửa phù hợp": "40 mm ~ 80 mm",
            "Backset": "60 mm & 70 mm",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Khóa Vân Tay Yale YDM4109A Chính Hãng Giá Rẻ Nhất | Livo Deco",
        "seoDescription": "Khóa vân tay Yale YDM4109A chính hãng ASSA ABLOY giá 9.800.000 đ tại Livo Deco. Cảm biến vân tay Liveness có nắp trượt bảo vệ, mã số ảo, bảo hành 24T tận nhà.",
        "seoContent": "### 1. Dòng khóa vân tay có nắp trượt bảo vệ biểu tượng của Yale\n**Yale YDM4109A** là phiên bản cải tiến vượt bậc từ dòng YDM4109 trứ danh, nổi bật với hệ thống nắp trượt cơ học bảo vệ mắt đọc vân tay khỏi bụi bẩn, ẩm mốc và ánh nắng trực tiếp. Thiết kế này giúp kéo dài tuổi thọ mắt đọc quang học lên gấp nhiều lần.\n\n### 2. Tính năng bảo mật thực chiến\nTích hợp đầy đủ các công nghệ an ninh đỉnh cao của tập đoàn ASSA ABLOY: quét vân tay Liveness 3 trong 1 phát hiện nhịp tim sống, mã số ảo PIN code, còi báo động chống phá khóa 80dB và hỗ trợ chìa cơ vi tính chống sao chép.",
        "infographics": [],
        "geoSummary": [
            "Model: Khóa điện tử Yale YDM4109A (YALE CATALOGUE 2025).",
            "Giá niêm yết: 9,800,000 đ | Bảo hành 24 tháng chính hãng.",
            "Kích thước: 68.6 x 320.7 x 40.1 mm | Cửa dày 40-80mm."
        ],
        "localGeo": {
            "south": "Showroom Livo Deco TP.HCM và các quận huyện nội ngoại thành.",
            "north_central": "Khu vực Hà Nội, Đà Nẵng, Hải Phòng.",
            "sla": "Lắp đặt tiêu chuẩn chuẩn hãng trong 2 giờ."
        },
        "faqs": [
            {
                "q": "1. Nắp trượt của Yale YDM4109A có ưu điểm gì?",
                "a": "Nắp trượt bảo vệ mắt đọc vân tay giúp chống lại bụi bẩn, mưa tạt hoặc trầy xước va chạm cơ học, đặc biệt hữu ích khi lắp đặt tại nhà phố hoặc hành lang chung cư có gió bụi."
            }
        ]
    },
    {
        "id": "yale-005",
        "slug": "khoa-dien-tu-yale-zuri",
        "name": "Khóa điện tử Yale ZURI Tích Hợp Bluetooth",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-tay-gat",
        "categoryName": "Khóa Thông Minh YALE Bluetooth",
        "price": "7,500,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-zuri.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 22",
        "badge": "Built-in Bluetooth YALE",
        "features": [
            "Tích hợp sẵn Module Bluetooth (Built-in) bên trong bo mạch – Quản lý khóa trực tiếp trên app điện thoại không tốn phí mua thêm module",
            "Cảm biến vân tay Liveness 3 trong 1 (Pixel + Live Finger + Heart rate)",
            "Mở khóa: Vân tay (100), Mã số PIN (100), Thẻ từ RFID (100), App Bluetooth, Chìa cơ",
            "Cổng cấp nguồn khẩn cấp USB-C tiện lợi và hiện đại",
            "Màu hoàn thiện: Matt Black (Đen mờ thanh lịch)",
            "Độ dày cửa: 40 - 100mm, Backset 60mm",
            "Khóa tự động và cảnh báo pin yếu thông minh"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa thông minh Yale ZURI Built-in Bluetooth",
            "Mã hiệu": "05/107103V/BL (B2B) / 05/107100/BL (B2C)",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Phương thức mở khóa": "App Bluetooth tích hợp sẵn, Vân tay Liveness, Thẻ từ RFID, Mã số ảo, Chìa cơ",
            "Dung lượng bộ nhớ": "100 vân tay, 100 thẻ từ, 100 mã số",
            "Kích thước mặt ngoài": "70 mm (Rộng) x 320 mm (Cao) x 27 mm (Sâu)",
            "Kích thước mặt trong": "70 mm (Rộng) x 320 mm (Cao) x 37 mm (Sâu)",
            "Độ dày cửa phù hợp": "40 mm ~ 100 mm",
            "Backset": "60 mm",
            "Cổng sạc khẩn cấp": "USB-C",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Khóa Thông Minh Yale ZURI Tích Hợp Bluetooth | Livo Deco",
        "seoDescription": "Khóa điện tử thông minh Yale ZURI chính hãng giá 7.500.000 đ tại Livo Deco. Tích hợp sẵn Bluetooth mở bằng điện thoại, vân tay Liveness 3-in-1, cổng sạc USB-C, bảo hành 24T.",
        "seoContent": "### 1. Giải pháp khóa thông minh toàn diện với Bluetooth tích hợp sẵn\n**Yale ZURI** là dòng khóa thế hệ mới trong **YALE CATALOGUE 2025** được trang bị sẵn Module Bluetooth ngay trên bo mạch chủ. Người dùng không cần phải tốn thêm chi phí mua phụ kiện rời mà vẫn dễ dàng cài đặt vân tay, chia sẻ mã số và mở khóa từ điện thoại thông minh qua ứng dụng chính hãng của Yale.\n\n### 2. Thiết kế hiện đại & Cổng sạc khẩn cấp USB-C\nKhóa sở hữu độ mỏng ấn tượng chỉ 27mm ở mặt ngoài cùng tông màu đen mờ hiện đại. Đáy khóa trang bị cổng USB-C tiện lợi, dễ dàng dùng chung dây cáp điện thoại khi cần cấp nguồn khẩn cấp.",
        "infographics": [],
        "geoSummary": [
            "Model: Khóa thông minh Yale ZURI Built-in Bluetooth.",
            "Giá niêm yết: 7,500,000 đ | Bảo hành 24 tháng.",
            "Tương thích: Cửa gỗ, cửa thép đố 40-100mm, Backset 60mm."
        ],
        "localGeo": {
            "south": "Showroom Livo Deco TP.HCM (Quận 1, 2, 7, Bình Thạnh, Thủ Đức...).",
            "north_central": "Hà Nội, Đà Nẵng và 63 tỉnh thành.",
            "sla": "Lắp đặt hoàn thiện trong 2 giờ."
        },
        "faqs": [
            {
                "q": "1. Khóa Yale ZURI có cần mua thêm module Bluetooth không?",
                "a": "Không cần. Yale ZURI đã được tích hợp sẵn vi xử lý Bluetooth bên trong khóa, giúp bạn kết nối và quản lý người dùng bằng điện thoại ngay khi lắp đặt xong."
            }
        ]
    },
    {
        "id": "yale-006",
        "slug": "khoa-dien-tu-yale-ydma-100np",
        "name": "Khóa điện tử Yale YDMA 100NP Cho Cửa Nhôm Xingfa Đố Hẹp",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-cua-nhom",
        "categoryName": "Khóa Cửa Nhôm Xingfa YALE",
        "price": "6,800,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-ydma-100np.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 23",
        "badge": "Chuyên Cửa Nhôm Xingfa",
        "features": [
            "Thiết kế thân siêu mỏng với bề rộng mặt khóa chỉ 34mm – Chuyên dụng hoàn hảo cho cửa nhôm Xingfa, cửa sắt, cửa trượt đố hẹp",
            "Khoảng cách từ mép cửa đến tâm khóa (Backset) siêu ngắn chỉ 35mm",
            "Cảm biến vân tay Liveness 3 trong 1 nhận diện nhịp tim và vân tay sống",
            "Phương thức mở: Vân tay (100), Thẻ từ RFID & Mã số PIN (100), Chìa cơ khẩn cấp",
            "Cổng cấp nguồn ngoài khẩn cấp cổng USB-C thế hệ mới",
            "Chất liệu hợp kim đúc chống ăn mòn và chống nước bề mặt",
            "Tự động khóa khi đóng cửa và chuông báo động chống cạy 80dB",
            "Màu hoàn thiện: Matt Black (Đen mờ sang trọng)"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa điện tử cửa nhôm Xingfa Yale YDMA 100NP",
            "Mã hiệu": "YDMA 100NP",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Phương thức mở khóa": "Vân tay Liveness 3-in-1, Thẻ từ RFID & Mã số PIN, Chìa cơ",
            "Dung lượng bộ nhớ": "100 vân tay, 100 thẻ từ & mã số",
            "Kích thước mặt ngoài": "34 mm (Rộng) x 328 mm (Cao) x 22 mm (Sâu)",
            "Kích thước mặt trong": "34 mm (Rộng) x 328 mm (Cao) x 16 mm (Sâu)",
            "Khoảng cách tâm khóa (Backset)": "35 mm (Chuẩn đố hẹp cửa nhôm)",
            "Độ dày cửa phù hợp": "40 mm ~ 90 mm",
            "Chất liệu": "Hợp kim kẽm chống oxy hóa",
            "Cổng nguồn dự phòng": "USB-C",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Khóa Vân Tay Cửa Nhôm Xingfa Yale YDMA 100NP Chính Hãng | Livo Deco",
        "seoDescription": "Khóa điện tử Yale YDMA 100NP chuyên dụng cho cửa nhôm Xingfa, cửa trượt đố hẹp bề rộng 34mm, Backset 35mm. Vân tay Liveness, thẻ từ, mã số, giá 6.800.000 đ, bảo hành 24T.",
        "seoContent": "### 1. Giải pháp khóa vân tay hàng đầu cho cửa nhôm Xingfa & Cửa sắt đố hẹp\nCác dòng cửa nhôm kính hệ Xingfa, PMI, Topal hay cửa sắt đố hẹp thường có bề rộng thanh nhôm chỉ từ 50mm - 60mm, khiến các loại khóa thông thường không thể lắp đặt vừa. **Yale YDMA 100NP** ra đời nhằm giải quyết triệt để bài toán này với bề ngang mặt khóa siêu mỏng chỉ **34mm** và Backset **35mm**, ôm khít thanh nhôm hoàn hảo mà không làm biến dạng khung cửa.\n\n### 2. Công nghệ bảo mật chuẩn ASSA ABLOY Hoa Kỳ\nDù có ngoại hình thon gọn, Yale YDMA 100NP vẫn được tích hợp trọn vẹn công nghệ quét vân tay **Liveness 3 trong 1** đỉnh cao, chuông báo động 80dB và cổng nguồn khẩn cấp USB-C hiện đại.",
        "infographics": [],
        "geoSummary": [
            "Model: Khóa vân tay cửa nhôm Yale YDMA 100NP.",
            "Bề rộng mặt khóa: 34mm | Backset: 35mm | Độ dày cửa: 40-90mm.",
            "Giá niêm yết: 6,800,000 đ | Bảo hành chính hãng 24 tháng."
        ],
        "localGeo": {
            "south": "TP.HCM, Bình Dương, Đồng Nai, Vũng Tàu, Long An.",
            "north_central": "Hà Nội, Hải Phòng, Đà Nẵng.",
            "sla": "Lắp đặt chuẩn kỹ thuật cửa nhôm Xingfa trong 2 giờ."
        },
        "faqs": [
            {
                "q": "1. Khóa Yale YDMA 100NP có lắp được cho cửa nhôm Xingfa hệ 55 không?",
                "a": "Hoàn toàn phù hợp. Nhờ bề rộng chỉ 34mm và backset 35mm, Yale YDMA 100NP được thiết kế chuyên biệt cho hệ nhôm Xingfa 55, cửa nhôm trượt lùa và cửa sắt hộp đố hẹp."
            }
        ]
    },
    {
        "id": "yale-007",
        "slug": "khoa-dien-tu-yale-ydme-100-nxt",
        "name": "Khóa điện tử Yale YDME 100 NXT Vân Tay 1 Chạm Trên Tay Cầm",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-tay-gat",
        "categoryName": "Khóa Thông Minh YALE Một Chạm",
        "price": "5,600,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-ydme-100-nxt.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 24",
        "badge": "Vân Tay 1 Chạm 2025",
        "features": [
            "Cảm biến vân tay tròn công nghệ sinh trắc học đặt ngay trên trục tay nắm – Mở khóa và vặn cửa chỉ trong 1 thao tác duy nhất",
            "Mở khóa đa dạng: Vân tay (100), Mã số PIN (100), Thẻ từ RFID (100), Chìa cơ khẩn cấp",
            "Vòng đèn LED hiển thị trạng thái sinh động bao quanh cảm biến vân tay",
            "Cổng cấp nguồn khẩn cấp USB-C ở đáy khóa",
            "Báo động 80dB khi có hiện tượng phá khóa hoặc nhập sai nhiều lần",
            "Màu hoàn thiện: Black (Đen nguyên khối)",
            "Tương thích độ dày cửa 40 - 65mm, Backset 60mm"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa thông minh vân tay 1 chạm Yale YDME 100 NXT",
            "Mã hiệu": "YDME 100 NXT",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Phương thức mở khóa": "Vân tay trên tay nắm, Mã số ảo, Thẻ từ RFID, Chìa cơ",
            "Dung lượng bộ nhớ": "100 vân tay, 100 mã số, 100 thẻ từ",
            "Kích thước mặt ngoài": "80 mm (Rộng) x 375 mm (Cao) x 30 mm (Sâu)",
            "Kích thước mặt trong": "80 mm (Rộng) x 375 mm (Cao) x 30 mm (Sâu)",
            "Backset": "60 mm",
            "Độ dày cửa phù hợp": "40 mm ~ 65 mm",
            "Cổng cấp nguồn khẩn cấp": "USB-C",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Khóa Vân Tay Yale YDME 100 NXT Giá Rẻ Chính Hãng | Livo Deco",
        "seoDescription": "Khóa điện tử vân tay Yale YDME 100 NXT chính hãng giá chỉ 5.600.000 đ tại Livo Deco. Cảm biến vân tay 1 chạm trên tay gạt, thẻ từ, mã số, cổng sạc USB-C, bảo hành 24T.",
        "seoContent": "### 1. Trải nghiệm mở cửa 1 chạm cực kỳ tự nhiên với Yale YDME 100 NXT\n**Yale YDME 100 NXT** sở hữu thiết kế thông minh với cảm biến vân tay tròn đặt ngay tại vị trí ngón tay cái khi cầm vào tay nắm. Bạn chỉ cần đặt ngón tay vào cảm biến và đồng thời gạt nhẹ tay nắm xuống là cửa mở ngay lập tức, mang lại cảm giác mở cửa nhanh chóng và mượt mà nhất trong dòng khóa thông minh.\n\n### 2. Thiết kế vuông vức mạnh mẽ & Đầy đủ tính năng\nVới mức giá cực kỳ cạnh tranh chỉ **5,600,000 đ**, sản phẩm phù hợp hoàn hảo cho căn hộ chung cư, cửa phòng ngủ biệt thự và văn phòng làm việc với tiêu chuẩn chất lượng nghiêm ngặt của ASSA ABLOY.",
        "infographics": [],
        "geoSummary": [
            "Model: Khóa điện tử Yale YDME 100 NXT (Vân tay 1 chạm).",
            "Giá niêm yết: 5,600,000 đ | Bảo hành 24 tháng tận nơi.",
            "Kích thước: 80 x 375 x 30 mm | Cửa dày 40-65mm | Backset 60mm."
        ],
        "localGeo": {
            "south": "TP.HCM và các tỉnh miền Nam.",
            "north_central": "Hà Nội, Đà Nẵng và miền Bắc.",
            "sla": "Lắp đặt hoàn thiện sau 2 giờ."
        },
        "faqs": [
            {
                "q": "1. Vân tay đặt trên tay nắm của Yale YDME 100 NXT có dễ sử dụng không?",
                "a": "Rất tiện lợi và tự nhiên. Khi bạn đưa tay nắm cửa, ngón cái tự động chạm vào mắt đọc vân tay, khóa nhận diện và mở chốt trong 0.3 giây, bạn chỉ việc gạt tay xuống để bước vào nhà."
            }
        ]
    },
    {
        "id": "yale-008",
        "slug": "khoa-dien-tu-yale-ydme-200-nxt",
        "name": "Khóa điện tử Yale YDME 200 NXT Viền Vàng Gold Bo Cong",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-tay-gat",
        "categoryName": "Khóa Thông Minh YALE Luxury",
        "price": "6,200,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-ydme-200-nxt.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 25",
        "badge": "Thiết Kế Gold Line 2025",
        "features": [
            "Ngôn ngữ thiết kế bo cong mềm mại với đường chỉ viền mạ vàng Gold sang trọng (Black, Gold line)",
            "Cảm biến vân tay 1 chạm tròn trên tay nắm có viền kim loại ánh kim",
            "Phương thức mở khóa: Vân tay (100), Mã số PIN (100), Thẻ từ RFID (100), Chìa cơ",
            "Cổng cấp nguồn khẩn cấp USB-C hiện đại",
            "Khóa tự động và chuông còi báo động 80dB",
            "Độ dày cửa 40 - 65mm, Backset 60mm"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa thông minh Yale YDME 200 NXT Gold Line",
            "Mã hiệu": "YDME 200 NXT",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Phương thức mở khóa": "Vân tay trên tay nắm, Thẻ từ RFID, Mã số ảo, Chìa cơ",
            "Dung lượng bộ nhớ": "100 vân tay, 100 thẻ từ, 100 mã số",
            "Kích thước mặt ngoài": "80 mm (Rộng) x 375 mm (Cao) x 30 mm (Sâu)",
            "Kích thước mặt trong": "80 mm (Rộng) x 375 mm (Cao) x 30 mm (Sâu)",
            "Màu sắc": "Đen phối viền vàng kim sang trọng (Black, Gold line)",
            "Backset": "60 mm",
            "Độ dày cửa phù hợp": "40 mm ~ 65 mm",
            "Nguồn dự phòng": "Cổng sạc USB-C",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Khóa Điện Tử Yale YDME 200 NXT Viền Vàng Gold Chính Hãng | Livo Deco",
        "seoDescription": "Khóa điện tử Yale YDME 200 NXT chính hãng giá 6.200.000 đ tại Livo Deco. Thiết kế bo cong viền vàng Gold Luxury, vân tay 1 chạm, thẻ từ, mã số, bảo hành 24T tận nhà.",
        "seoContent": "### 1. Nét chấm phá sang trọng với đường nét Gold Line tinh tế\n**Yale YDME 200 NXT** kế thừa toàn bộ ưu điểm thao tác một chạm của dòng NXT nhưng được nâng tầm thẩm mỹ với các góc bo tròn duyên dáng và đường viền kim loại mạ vàng Gold chạy dọc thân khóa. Đây là lựa chọn hoàn hảo cho những gia chủ yêu thích sự thanh thoát, tinh tế và sang trọng trong kiến trúc nội thất.",
        "infographics": [],
        "geoSummary": [
            "Model: Khóa điện tử Yale YDME 200 NXT (Gold Line).",
            "Giá niêm yết: 6,200,000 đ | Bảo hành 24 tháng.",
            "Kích thước: 80 x 375 x 30 mm | Backset 60mm | Cửa dày 40-65mm."
        ],
        "localGeo": {
            "south": "TP.HCM, Bình Dương, Đồng Nai.",
            "north_central": "Hà Nội, Đà Nẵng, Quảng Ninh.",
            "sla": "Lắp đặt tận nhà trong 2 giờ."
        },
        "faqs": [
            {
                "q": "1. Điểm khác biệt giữa YDME 100 NXT và YDME 200 NXT là gì?",
                "a": "YDME 100 NXT có thiết kế góc vuông mạnh mẽ toàn thân màu đen, trong khi YDME 200 NXT được bo tròn 4 góc mềm mại kết hợp đường chỉ viền màu vàng Gold cao cấp tạo điểm nhấn nghệ thuật."
            }
        ]
    },
    {
        "id": "yale-009",
        "slug": "khoa-dien-tu-yale-ydd724a",
        "name": "Khóa điện tử Yale YDD724A Chốt Deadbolt Không Tay Nắm",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-tay-gat",
        "categoryName": "Khóa Chốt Điện Tử YALE Deadbolt",
        "price": "5,900,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-ydd724a.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 26",
        "badge": "Khóa Phụ Deadbolt YALE",
        "features": [
            "Dòng khóa chốt độc lập (Deadbolt) nhỏ gọn, chuyên dùng làm khóa phụ tăng cường an ninh cấp độ cao",
            "Có thể lắp độc lập hoặc kết hợp cùng các loại tay nắm gạt cơ / tay nắm kéo cửa đại sảnh",
            "Cảm biến vân tay Liveness 3 trong 1 (Pixel + Live Finger + Heart rate)",
            "Mở khóa: Vân tay (100), Mã số (100), Thẻ từ RFID (100), Chìa cơ, Tùy chọn Bluetooth",
            "Kích thước cực kỳ nhỏ gọn: Mặt ngoài chỉ cao 176mm, rộng 66mm",
            "Báo động âm lượng lớn 80dB và chức năng mã số ảo chống nhìn trộm",
            "Hỗ trợ kích pin khẩn cấp 9V"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa chốt điện tử Deadbolt Yale YDD724A",
            "Mã hiệu": "YDD724A",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Phương thức mở khóa": "Vân tay Liveness 3-in-1, Mã số ảo, Thẻ từ RFID, Chìa cơ, Tùy chọn Bluetooth",
            "Dung lượng bộ nhớ": "100 vân tay, 100 mã số, 100 thẻ từ",
            "Kích thước mặt ngoài": "66 mm (Rộng) x 176 mm (Cao) x 31.5 mm (Sâu)",
            "Kích thước mặt trong": "70 mm (Rộng) x 170 mm (Cao) x 35 mm (Sâu)",
            "Backset": "60 mm & 70 mm",
            "Độ dày cửa phù hợp": "45 mm ~ 57 mm",
            "Màu hoàn thiện": "Black (Đen nhám)",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Khóa Chốt Điện Tử Yale YDD724A Deadbolt Chính Hãng | Livo Deco",
        "seoDescription": "Khóa chốt điện tử Yale YDD724A Deadbolt chính hãng giá 5.900.000 đ tại Livo Deco. Nhỏ gọn, vân tay Liveness 3-in-1, thẻ từ, mã số ảo, tăng cường an ninh tối đa, bảo hành 24T.",
        "seoContent": "### 1. Giải pháp khóa phụ Deadbolt bảo vệ 2 lớp an toàn vượt trội\nĐối với những gia chủ đã có sẵn bộ tay nắm cửa kéo đại sảnh đắt tiền hoặc muốn nhân đôi sự an toàn cho ngôi nhà, **Yale YDD724A** là giải pháp khóa chốt điện tử hoàn hảo. Với cơ chế chốt thép Deadbolt ăn sâu vào khung tường, kẻ gian hoàn toàn bất lực trước các thủ đoạn cạy mép cửa.\n\n### 2. Thiết kế nhỏ gọn, hiện đại\nKích thước mặt ngoài chỉ 66 x 176mm, Yale YDD724A nằm gọn gàng trên cánh cửa mà vẫn sở hữu trọn bộ công nghệ bảo mật cao cấp nhất của Yale.",
        "infographics": [],
        "geoSummary": [
            "Model: Khóa chốt điện tử Yale YDD724A Deadbolt.",
            "Giá niêm yết: 5,900,000 đ | Bảo hành 24 tháng.",
            "Kích thước nhỏ gọn: 66 x 176 x 31.5 mm | Cửa dày 45-57mm."
        ],
        "localGeo": {
            "south": "Showroom Livo Deco TP.HCM và các tỉnh lân cận.",
            "north_central": "Hà Nội, Đà Nẵng, Hải Phòng.",
            "sla": "Lắp đặt nhanh trong 2 giờ."
        },
        "faqs": [
            {
                "q": "1. Khóa Yale YDD724A có tay nắm không?",
                "a": "Không, Yale YDD724A là dạng khóa chốt Deadbolt không tay nắm, thường được lắp phía trên tay nắm gạt hoặc tay nắm kéo cơ để làm khóa thông minh bảo vệ chính."
            }
        ]
    },
    {
        "id": "yale-010",
        "slug": "khoa-dien-tu-yale-ydr413a",
        "name": "Khóa điện tử Yale YDR413A Cho Cửa Kính Cường Lực Không Khung",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "khoa-cua-kinh",
        "categoryName": "Khóa Cửa Kính YALE",
        "price": "6,900,000 đ",
        "image": "images/products_png/khoa-dien-tu-yale-ydr413a.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 27",
        "badge": "Chuyên Dụng Cửa Kính",
        "features": [
            "Chuyên dụng cho cửa kính cường lực không khung (Frameless Glass Door) độ dày từ 9mm đến 13mm",
            "Lắp đặt dạng kẹp thông minh – Tuyệt đối không cần khoan đục cắt khoét tấm kính cường lực",
            "Cảm biến vân tay Liveness 3 trong 1 (Pixel + Live Finger + Heart rate)",
            "Mở khóa: Vân tay (100), Mã số PIN (100), Tùy chọn Bluetooth điều khiển qua điện thoại",
            "Vỏ hoàn thiện màu Silver (Bạc ánh kim) đồng điệu với kẹp kính và phụ kiện inox văn phòng",
            "Báo động 80dB khi bị cạy hoặc tác động lực mạnh lên mặt kính",
            "Cảnh báo pin yếu và cổng kích pin 9V"
        ],
        "specs": {
            "Tên sản phẩm": "Khóa điện tử cửa kính cường lực Yale YDR413A (YDG413A)",
            "Mã hiệu": "YDG413A / YDR413A",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Phương thức mở khóa": "Vân tay Liveness 3-in-1, Mã số ảo PIN code, Tùy chọn Bluetooth",
            "Dung lượng bộ nhớ": "100 vân tay, 100 mã số",
            "Kích thước mặt ngoài": "72.8 mm (Rộng) x 186 mm (Cao) x 14 mm (Sâu)",
            "Kích thước mặt trong": "77.5 mm (Rộng) x 190.5 mm (Cao) x 48.8 mm (Sâu)",
            "Độ dày kính tương thích": "9 mm ~ 13 mm (Kính cường lực)",
            "Màu hoàn thiện": "Silver (Màu bạc sang trọng)",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Khóa Cửa Kính Vân Tay Yale YDR413A Không Cần Khoan Kính | Livo Deco",
        "seoDescription": "Khóa điện tử cửa kính Yale YDR413A chính hãng giá 6.900.000 đ tại Livo Deco. Lắp đặt kẹp kính 9-13mm không khoan đục, vân tay Liveness, mã số ảo, bảo hành 24T toàn quốc.",
        "seoContent": "### 1. Khóa vân tay chuyên dụng cửa kính cường lực văn phòng & Cửa hàng\nĐối với cửa kính cường lực không khung tại các văn phòng công ty, showroom và nhà phố, việc khoan cắt kính sau khi tôi nhiệt là điều bất khả thi vì sẽ làm vỡ nổ tấm kính. **Yale YDR413A (YDG413A)** sử dụng công nghệ kẹp kính độc quyền của Yale, siết chặt bằng hệ thống ốc cố định và giác hút chân không, bảo đảm độ bám chắc chắn tuyệt đối mà không cần tạo bất kỳ lỗ khoan nào trên kính.\n\n### 2. Thiết kế siêu mỏng & Công nghệ vân tay Liveness\nMặt ngoài khóa chỉ dày 14mm, phủ màu bạc ánh kim tinh tế. Cảm biến Liveness 3 trong 1 quét vân tay nhanh chóng chỉ trong tích tắc, giúp quản lý nhân sự văn phòng và bảo vệ tài sản doanh nghiệp an toàn tối đa.",
        "infographics": [],
        "geoSummary": [
            "Model: Khóa điện tử cửa kính Yale YDR413A / YDG413A.",
            "Độ dày kính: 9-13mm (Kẹp kính không khoan đục) | Màu bạc Silver.",
            "Giá niêm yết: 6,900,000 đ | Bảo hành chính hãng 24 tháng."
        ],
        "localGeo": {
            "south": "TP.HCM (Tòa nhà văn phòng Quận 1, 3, 7, Bình Thạnh, Thủ Đức...).",
            "north_central": "Hà Nội, Đà Nẵng, Hải Phòng.",
            "sla": "Lắp đặt kẹp kính chuẩn xác trong 1 giờ."
        },
        "faqs": [
            {
                "q": "1. Lắp khóa Yale YDR413A có cần phải khoan kính không?",
                "a": "Hoàn toàn không. Khóa sử dụng cơ chế ngàm kẹp chuyên dụng cho kính cường lực 9mm - 13mm, siết chặt và dán lớp đệm cao su bảo vệ, không cần khoan cắt bất kỳ chi tiết nào."
            }
        ]
    },
    {
        "id": "yale-011",
        "slug": "tay-day-hoi-yale-yic-2124",
        "name": "Tay Đẩy Hơi Đóng Cửa Tự Động Yale YIC-2124 Chống Cháy",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "tay-day-hoi",
        "categoryName": "Phụ Kiện Cửa & Tay Đẩy Hơi YALE",
        "price": "1,250,000 đ",
        "image": "images/products_png/tay-day-hoi-yale-yic-2124.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 106",
        "badge": "Chuẩn Chống Cháy EN",
        "features": [
            "Đạt tiêu chuẩn chất lượng châu Âu CE và chứng nhận chống cháy EN 1154 & EN 1634",
            "Tải trọng cửa tối đa lên đến 80kg, tương thích chiều rộng cửa 750mm - 1100mm",
            "Điều chỉnh lực đóng linh hoạt (Closing force size EN 2 - 4)",
            "Tích hợp 2 van điều chỉnh độc lập: Điều chỉnh tốc độ đóng cửa & Điều chỉnh tốc độ chốt (sập)",
            "Góc mở cửa tối đa lên đến 180 độ, góc giữ cửa 70 - 145 độ",
            "Phù hợp cho cả cửa mở trái và mở phải (DIN Left & DIN Right)",
            "Có 2 phiên bản: Có chức năng giữ cửa (Hold-open) và Không giữ cửa chuyên dùng cửa chống cháy"
        ],
        "specs": {
            "Tên sản phẩm": "Cơ cấu đóng cửa tự động tay đẩy hơi Yale YIC-2124",
            "Mã hiệu": "YIC-2124 (Không giữ cửa) / YIC-2124HO (Có giữ cửa Hold-open)",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Lực đẩy": "EN 2 - 4",
            "Chiều rộng cửa phù hợp": "750 mm ~ 1100 mm",
            "Trọng lượng cửa tối đa": "80 kg",
            "Góc mở tối đa": "180 độ",
            "Góc giữ cửa": "70 độ ~ 145 độ",
            "Tiêu chuẩn chứng nhận": "EN 1154, EN 1634, Tiêu chuẩn CE Châu Âu",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Tay Đẩy Hơi Yale YIC-2124 Chống Cháy Đóng Cửa Tự Động | Livo Deco",
        "seoDescription": "Tay đẩy hơi Yale YIC-2124 chính hãng ASSA ABLOY giá 1.250.000 đ tại Livo Deco. Đạt chuẩn chống cháy EN 1154/EN 1634, tải trọng 80kg, điều chỉnh 2 tốc độ, bảo hành 24T.",
        "seoContent": "### 1. Cơ cấu đóng cửa tự động tiêu chuẩn an toàn phòng cháy chữa cháy\n**Tay đẩy hơi Yale YIC-2124** (Surface Door Closer) là thiết bị không thể thiếu cho cửa thoát hiểm, cửa thép ngăn cháy chung cư, cửa phòng kỹ thuật và cửa văn phòng. Sản phẩm đạt chứng nhận chống cháy khắt khe **EN 1154** và **EN 1634**, đảm bảo cánh cửa luôn tự động khép kín hoàn toàn để ngăn khói độc và lửa lan khi có hỏa hoạn.\n\n### 2. Vận hành êm ái, bền bỉ đến 500.000 chu kỳ\nTrang bị piston thủy lực gia công chính xác từ hợp kim nhôm đúc, vận hành êm ái không gây tiếng va đập mạnh, tuổi thọ kiểm nghiệm trên 500.000 lần đóng mở.",
        "infographics": [],
        "geoSummary": [
            "Model: Tay đẩy hơi Yale YIC-2124 (Chống cháy EN 1154).",
            "Giá niêm yết: 1,250,000 đ | Tải trọng 80kg | Bảo hành 24 tháng."
        ],
        "localGeo": {
            "south": "Showroom Livo Deco TP.HCM và dự án miền Nam.",
            "north_central": "Hà Nội, Đà Nẵng và toàn quốc.",
            "sla": "Cung cấp số lượng lớn cho công trình trong 24h."
        },
        "faqs": [
            {
                "q": "1. Tay đẩy hơi Yale YIC-2124 có lắp được cho cửa mở trái và mở phải không?",
                "a": "Có. Yale YIC-2124 được thiết kế đối xứng thông minh, phù hợp lắp đặt linh hoạt cho cả cửa mở trái (DIN Left) và cửa mở phải (DIN Right)."
            }
        ]
    },
    {
        "id": "yale-012",
        "slug": "cau-noi-yale-connect-plus-hub-2-wifi",
        "name": "Cầu Nối Wifi Yale Connect Plus Hub 2 - Điều Khiển Khóa Từ Xa",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "phu-kien-yale",
        "categoryName": "Phụ Kiện Nhà Thông Minh YALE",
        "price": "1,850,000 đ",
        "image": "images/products_png/cau-noi-yale-connect-plus-hub-2-wifi.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 28",
        "badge": "Phụ Kiện Chính Hãng",
        "features": [
            "Cầu nối Internet Wifi thế hệ mới nhất dành cho hệ sinh thái khóa thông minh Yale",
            "Điều khiển đóng mở khóa cửa từ xa ở bất cứ đâu trên thế giới qua ứng dụng Yale Home / Yale Access",
            "Nhận thông báo trạng thái khóa tức thì về điện thoại khi có người mở cửa",
            "Hỗ trợ điều khiển bằng giọng nói qua trợ lý ảo Google Assistant và Amazon Alexa",
            "Tạo và quản lý mật mã tạm thời cho khách, người giúp việc theo khung giờ",
            "Kết nối đồng thời nhiều thiết bị khóa trong phạm vi sóng không dây"
        ],
        "specs": {
            "Tên sản phẩm": "Cầu nối Wifi Yale Connect Plus Hub 2",
            "Mã hiệu": "YAR/SWAA/HUB-A",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Chuẩn kết nối": "Wifi 2.4GHz & Bluetooth 5.0",
            "Nguồn điện": "Cắm trực tiếp ổ cắm 100V - 240V AC",
            "Tương thích ứng dụng": "Yale Home (iOS / Android)",
            "Hệ sinh thái thông minh": "Google Assistant, Amazon Alexa, Apple Siri Shortcuts",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Cầu Nối Wifi Yale Connect Plus Hub 2 Chính Hãng | Livo Deco",
        "seoDescription": "Cầu nối Wifi Yale Connect Plus Hub 2 chính hãng ASSA ABLOY giá 1.850.000 đ tại Livo Deco. Mở khóa từ xa qua Internet, thông báo điện thoại, tích hợp Google Assistant.",
        "seoContent": "### 1. Nâng tầm khóa điện tử thành hệ sinh thái nhà thông minh đỉnh cao\n**Yale Connect Plus Hub 2** kết nối trực tiếp ổ khóa Yale của bạn với mạng Wifi gia đình và nền tảng điện toán đám mây Yale Cloud. Giờ đây, dù bạn đang ở cơ quan, đi du lịch hay công tác nước ngoài, việc kiểm tra cửa đã đóng chưa hay mở cửa từ xa cho người thân chỉ mất 1 giây trên màn hình smartphone.",
        "infographics": [],
        "geoSummary": [
            "Model: Yale Connect Plus Hub 2 - Wifi (Mã: YAR/SWAA/HUB-A).",
            "Giá: 1,850,000 đ | Bảo hành chính hãng 24 tháng."
        ],
        "localGeo": {
            "south": "TP.HCM và các tỉnh phía Nam.",
            "north_central": "Hà Nội, Đà Nẵng và toàn quốc.",
            "sla": "Giao hàng và cài đặt hướng dẫn tận nhà."
        },
        "faqs": [
            {
                "q": "1. Yale Connect Plus Hub 2 cắm cách ổ khóa bao xa thì hoạt động tốt?",
                "a": "Khoảng cách khuyến nghị từ Hub Wifi đến khóa cửa là trong vòng 3 - 5 mét không có tường chắn kim loại dày để đảm bảo tín hiệu Bluetooth kết nối luôn mạnh và ổn định nhất."
            }
        ]
    },
    {
        "id": "yale-013",
        "slug": "module-bluetooth-yale-home",
        "name": "Module Bluetooth Yale Home Cho Khóa Điện Tử",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "phu-kien-yale",
        "categoryName": "Phụ Kiện Khóa YALE",
        "price": "950,000 đ",
        "image": "images/products_png/module-bluetooth-yale-home.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 28",
        "badge": "Phụ Kiện Chính Hãng",
        "features": [
            "Module cắm mở rộng nâng cấp khóa điện tử Yale thành khóa thông minh điều khiển bằng điện thoại",
            "Quản lý lịch sử ra vào và cài đặt người dùng dễ dàng qua app Yale Home",
            "Tự động mở khóa khi bạn tiến lại gần cửa (Auto-unlock via Bluetooth)",
            "Dễ dàng lắp đặt chỉ bằng cách cắm vào khe cắm module có sẵn trong thân khóa",
            "Mã hiệu chính hãng: RFHX-YB7H0-00"
        ],
        "specs": {
            "Tên sản phẩm": "Module Bluetooth Yale Home",
            "Mã hiệu": "RFHX-YB7H0-00",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Chuẩn kết nối": "Bluetooth Low Energy (BLE 5.0)",
            "Tương thích dòng khóa": "Yale Luna Pro, Kyra Pro, YDM7116A, YDM4109A, YDD724A...",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Module Bluetooth Yale Home Chính Hãng RFHX-YB7H0-00 | Livo Deco",
        "seoDescription": "Module Bluetooth Yale Home chính hãng giá 950.000 đ tại Livo Deco. Nâng cấp khóa Yale mở qua điện thoại, cài đặt người dùng trên app Yale Home, bảo hành 24T.",
        "seoContent": "### 1. Phụ kiện nâng cấp kết nối Bluetooth cho khóa Yale\nVới thiết kế dạng cắm Plug-and-Play, **Module Bluetooth Yale Home (RFHX-YB7H0-00)** giúp khóa điện tử Yale của bạn giao tiếp trực tiếp với smartphone, biến chiếc điện thoại thành chìa khóa vạn năng tiện lợi.",
        "infographics": [],
        "geoSummary": [
            "Model: Module Bluetooth Yale Home (RFHX-YB7H0-00).",
            "Giá: 950,000 đ | Bảo hành 24 tháng."
        ],
        "localGeo": {
            "south": "TP.HCM và toàn quốc.",
            "north_central": "Hà Nội, Đà Nẵng.",
            "sla": "Giao hàng toàn quốc trong 24h."
        },
        "faqs": [
            {
                "q": "1. Lắp Module Bluetooth vào khóa Yale có khó không?",
                "a": "Rất đơn giản. Bạn chỉ cần tháo nắp pin của khóa, cắm module vào khe cắm có sẵn và mở ứng dụng Yale Home trên điện thoại để quét kết nối trong 1 phút."
            }
        ]
    },
    {
        "id": "yale-014",
        "slug": "module-smart-home-yale-zigbee",
        "name": "Module Nhà Thông Minh Yale Zigbee Kết Nối Smart Home",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "phu-kien-yale",
        "categoryName": "Phụ Kiện Nhà Thông Minh YALE",
        "price": "1,150,000 đ",
        "image": "images/products_png/module-smart-home-yale-zigbee.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 29",
        "badge": "Chuẩn Zigbee Alliance",
        "features": [
            "ASSA ABLOY là thành viên điều hành cấp cao của Hiệp hội Liên minh Zigbee toàn cầu",
            "Module tích hợp khóa Yale vào hệ thống nhà thông minh Zigbee (Tuya, Lumi, SmartThings, Home Assistant)",
            "Kích hoạt các ngữ cảnh thông minh tự động (ví dụ: mở khóa cửa thì đèn phòng khách bật sáng, rèm cửa mở ra và điều hòa khởi động)",
            "Giao thức sóng Zigbee tiêu thụ cực ít năng lượng, không làm hao pin khóa",
            "Mã sản phẩm: RFHX-YZB61-00"
        ],
        "specs": {
            "Tên sản phẩm": "Module điều khiển nhà thông minh Yale Zigbee",
            "Mã hiệu": "RFHX-YZB61-00",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Giao thức": "Zigbee 3.0",
            "Tương thích hệ sinh thái": "Samsung SmartThings, Tuya Smart, Lumi, Home Assistant...",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Module Zigbee Cho Khóa Yale RFHX-YZB61-00 Chính Hãng | Livo Deco",
        "seoDescription": "Module nhà thông minh Yale Zigbee RFHX-YZB61-00 chính hãng giá 1.150.000 đ tại Livo Deco. Kết nối SmartThings, Tuya, Home Assistant kích hoạt kịch bản tự động, bảo hành 24T.",
        "seoContent": "### 1. Đồng bộ khóa cửa Yale vào kịch bản Smart Home Zigbee\n**Module Yale Zigbee (RFHX-YZB61-00)** là cầu nối hoàn hảo giữa các dòng khóa thông minh Yale với hệ sinh thái nhà thông minh Zigbee. Bạn có thể dễ dàng thiết lập kịch bản về nhà hoặc rời nhà tự động hóa hoàn toàn.",
        "infographics": [],
        "geoSummary": [
            "Model: Module Yale Zigbee RFHX-YZB61-00.",
            "Giá: 1,150,000 đ | Bảo hành chính hãng 24 tháng."
        ],
        "localGeo": {
            "south": "Showroom Livo Deco TP.HCM và các đối tác Smarthome.",
            "north_central": "Hà Nội, Đà Nẵng.",
            "sla": "Hỗ trợ cấu hình tích hợp Smarthome 24/7."
        },
        "faqs": [
            {
                "q": "1. Khóa Yale dùng module Zigbee có kết nối được với Hub Tuya hay SmartThings không?",
                "a": "Có, module Yale Zigbee chuẩn Zigbee 3.0 tương thích tốt với các bộ điều khiển trung tâm Zigbee Gateway của Samsung SmartThings, Tuya, Aqara Hub và Home Assistant."
            }
        ]
    },
    {
        "id": "yale-015",
        "slug": "module-smart-home-yale-zwave-700",
        "name": "Module Nhà Thông Minh Yale Z-Wave 700 Series",
        "brand": "YALE",
        "category": "khoa-dien-tu-yale",
        "subCategory": "phu-kien-yale",
        "categoryName": "Phụ Kiện Nhà Thông Minh YALE",
        "price": "1,250,000 đ",
        "image": "images/products_png/module-smart-home-yale-zwave-700.png",
        "yale_catalogue": "YALE CATALOGUE 2025 - Trang 29",
        "badge": "Z-Wave Plus 700",
        "features": [
            "Chip xử lý Z-Wave 700 Series thế hệ mới nhất với phạm vi phủ sóng xa hơn và độ trễ phản hồi cực thấp",
            "Mã hóa bảo mật cấp độ ngân hàng Security 2 (S2) chống nghe lén và can thiệp sóng vô tuyến",
            "Tương thích với các bộ điều khiển Z-Wave Gateway hàng đầu thế giới (Fibaro Home Center, Vera, Hubitat...)",
            "Mã sản phẩm chính hãng: RFHX-YZW83-00"
        ],
        "specs": {
            "Tên sản phẩm": "Module điều khiển nhà thông minh Yale Z-Wave 700 Series",
            "Mã hiệu": "RFHX-YZW83-00",
            "Thương hiệu": "YALE (ASSA ABLOY Group - USA)",
            "Giao thức": "Z-Wave Plus 700 Series",
            "Tương thích": "Fibaro, Vera, Home Center, Hubitat...",
            "Bảo hành": "24 tháng chính hãng tại Livo Deco"
        },
        "seoTitle": "Module Yale Z-Wave 700 Series RFHX-YZW83-00 Chính Hãng | Livo Deco",
        "seoDescription": "Module Yale Z-Wave 700 Series RFHX-YZW83-00 giá 1.250.000 đ tại Livo Deco. Kết nối hệ thống nhà thông minh Fibaro, Hubitat, bảo mật S2, bảo hành 24T chính hãng.",
        "seoContent": "### 1. Đỉnh cao kết nối cho các hệ thống nhà thông minh tiêu chuẩn Z-Wave\nĐối với các biệt thự cao cấp sử dụng hệ thống nhà thông minh chuẩn **Z-Wave (Fibaro, Hubitat)**, **Module Yale Z-Wave 700 (RFHX-YZW83-00)** là sự lựa chọn số 1 về độ ổn định, khả năng truyền xuyên tường mạnh mẽ và chuẩn mã hóa S2 siêu bảo mật.",
        "infographics": [],
        "geoSummary": [
            "Model: Module Yale Z-Wave 700 Series (RFHX-YZW83-00).",
            "Giá: 1,250,000 đ | Bảo hành chính hãng 24 tháng."
        ],
        "localGeo": {
            "south": "TP.HCM và toàn quốc.",
            "north_central": "Hà Nội, Đà Nẵng.",
            "sla": "Hỗ trợ kỹ thuật Smarthome chuẩn hãng."
        },
        "faqs": [
            {
                "q": "1. Module Z-Wave 700 có ưu điểm gì so với dòng 500 cũ?",
                "a": "Dòng chip Z-Wave 700 Series có tầm phủ sóng xa hơn 50%, tốc độ phản hồi nhanh hơn 20%, tiết kiệm pin hơn và tích hợp chuẩn bảo mật S2 cao nhất của Z-Wave Alliance."
            }
        ]
    }
]

data["yale_products"] = yale_products

with open("products_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully added {len(yale_products)} Yale products to products_data.json!")
