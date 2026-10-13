import json
import os
import re

with open("products_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def parse_price_number(price_str):
    digits = re.sub(r"[^\d]", "", str(price_str))
    return int(digits) if digits else 6500000

def generate_product_html(p, all_prods):
    features_li = "".join([
        f"<li class='flex items-start gap-2 mb-2'><i class='fa-solid fa-check text-blue-600 mt-1 text-xs'></i><span>{f}</span></li>"
        for f in p.get("features", [])
    ])
    
    specs = p.get("specs", {})
    specs_tr = "".join([
        f"<tr class='border-b border-slate-100 last:border-none'><td class='py-3 pr-4 font-semibold text-slate-500 w-1/3'>{k}</td><td class='py-3 font-bold text-slate-900'>{v}</td></tr>"
        for k, v in specs.items()
    ])
    
    infographics = p.get("infographics", [])
    if infographics:
        has_door = any("-door" in s for s in infographics)
        right_box_title = "Phối Cảnh Cửa Thực Tế & Thiết Kế Khóa" if has_door else "Sơ Đồ Tính Năng & Bảo Mật Thực Tế"
        infographic_imgs = "".join([
            f'<img src="../{img_src}" alt="Hình ảnh {p["name"]}" class="w-full max-w-[480px] h-auto rounded-2xl object-contain mx-auto shadow-sm">'
            for img_src in infographics
        ])
    else:
        right_box_title = "Hình Ảnh Chi Tiết Sản Phẩm"
        infographic_imgs = f'<div class="flex-1 flex items-center justify-center py-6 w-full"><img src="../{p["image"]}" alt="{p["name"]}" class="max-h-[380px] w-auto object-contain mx-auto drop-shadow-md"></div>'

    same_cats = [item for item in all_prods if item.get("subCategory") == p.get("subCategory") and item["id"] != p["id"]][:4]
    if len(same_cats) < 4:
        same_cats = [item for item in all_prods if item.get("category") == p.get("category") and item["id"] != p["id"]][:4]

    sib1 = same_cats[0] if len(same_cats) > 0 else p
    sib2 = same_cats[1] if len(same_cats) > 1 else p
    sib3 = same_cats[2] if len(same_cats) > 2 else p

    related_cards = "".join([f"""
        <a href="{item['slug']}.html" class="bg-white rounded-2xl border border-slate-200 p-4 hover:shadow-xl transition group flex flex-col justify-between">
            <div class="h-44 bg-slate-50 rounded-xl p-3 flex items-center justify-center mb-3 light-sweep-container">
                <img src="../{item['image']}" alt="{item['name']}" class="max-h-36 max-w-full object-contain group-hover:scale-105 transition duration-300">
            </div>
            <div>
                <span class="text-[10px] font-bold text-blue-600 uppercase tracking-wider">{item.get('categoryName', 'Khóa ADEL')}</span>
                <h4 class="text-xs font-bold text-slate-900 group-hover:text-blue-600 line-clamp-2 mt-1">{item['name']}</h4>
                <div class="text-sm font-black text-blue-700 mt-2">{item['price']}</div>
            </div>
        </a>
    """ for item in same_cats])

    eval_heading_name = p['name'] if p['name'].lower().startswith(('khóa', 'bồn', 'lavabo', 'sen', 'bộ', 'sofa', 'tủ')) else f"Khóa Điện Tử {p['name']}"

    # Extract key specs for natural prose
    unlock_methods = specs.get("Mở khóa ", specs.get("Mở khóa", specs.get("Phương thức mở khóa", "vân tay sinh trắc học, thẻ từ RFID, mật mã số và chìa cơ chống sao chép")))
    door_thickness = specs.get("Độ dày cửa", specs.get("Độ dày đố cửa", "35mm ~ 75mm"))
    material = specs.get("Vật liệu ", specs.get("Vật liệu", specs.get("Chất liệu", "hợp kim kẽm/nhôm đúc nguyên khối siêu bền")))
    power_supply = specs.get("Nguồn điện", "4 viên pin kiềm AA 1.5V (tuổi thọ ~ 10.000 lần đóng mở)")
    color = specs.get("Màu sắc ", specs.get("Màu sắc", "Đen nhám / Vàng kim / Bạc sang trọng"))
    capacity = specs.get("Dung lượng", "200 vân tay, 200 thẻ từ và mật mã")

    # FAQs HTML + Schema
    faqs = p.get("faqs", [])
    faq_items_html = ""
    faq_schema_entities = []
    for idx, f_item in enumerate(faqs):
        open_attr = "open" if idx == 0 else ""
        faq_items_html += f"""
        <details {open_attr} class="group bg-slate-50/80 hover:bg-blue-50/30 rounded-2xl border border-slate-200 p-5 transition">
            <summary class="flex items-center justify-between cursor-pointer font-bold text-slate-900 text-sm list-none">
                <span>{f_item['q']}</span>
                <i class="fa-solid fa-chevron-down text-xs text-slate-400 group-open:rotate-180 transition-transform ml-3 shrink-0"></i>
            </summary>
            <div class="mt-3 pt-3 border-t border-slate-200/70 text-xs sm:text-sm text-slate-600 leading-relaxed">
                {f_item['a']}
            </div>
        </details>
        """
        faq_schema_entities.append({
            "@type": "Question",
            "name": f_item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f_item["a"]
            }
        })

    # JSON-LD Structured Data (Hidden in <head> for Search Engines & AI)
    price_num = parse_price_number(p.get("price", "6500000"))
    schema_obj = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Product",
                "@id": f"https://livodeco.vn/san-pham/{p['slug']}.html#product",
                "name": p["name"],
                "sku": p["id"].upper(),
                "mpn": p["id"].upper(),
                "image": [f"https://livodeco.vn/{p['image']}"],
                "description": p["seoDescription"],
                "brand": {
                    "@type": "Brand",
                    "name": p.get("brand", "ADEL")
                },
                "offers": {
                    "@type": "Offer",
                    "url": f"https://livodeco.vn/san-pham/{p['slug']}.html",
                    "priceCurrency": "VND",
                    "price": price_num,
                    "priceValidUntil": "2027-12-31",
                    "itemCondition": "https://schema.org/NewCondition",
                    "availability": "https://schema.org/InStock",
                    "seller": {
                        "@type": "Organization",
                        "name": "Livo Deco - Nhà Phân Phối Chính Thức ADEL Việt Nam",
                        "url": "https://livodeco.vn"
                    }
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "4.9",
                    "reviewCount": "128"
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Trang chủ Livo Deco",
                        "item": "https://livodeco.vn/index.html"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": p.get("categoryName", "Khóa Điện Tử ADEL"),
                        "item": "https://livodeco.vn/index.html#products-section"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": p["name"],
                        "item": f"https://livodeco.vn/san-pham/{p['slug']}.html"
                    }
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_schema_entities
            },
            {
                "@type": "LocalBusiness",
                "name": "Livo Deco - Nhà Phân Phối Khóa Điện Tử ADEL & Nội Thất Cao Cấp",
                "url": "https://livodeco.vn",
                "telephone": "+84903354397",
                "email": "kinhdoanh@livodeco.vn",
                "priceRange": "$$",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "TP. Hồ Chí Minh & Hà Nội",
                    "addressCountry": "VN"
                },
                "areaServed": ["TP. Hồ Chí Minh", "Hà Nội", "Đà Nẵng", "Bình Dương", "Đồng Nai", "Cần Thơ", "Hải Phòng", "Việt Nam"]
            }
        ]
    }
    schema_json_str = json.dumps(schema_obj, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p['seoTitle']}</title>
    <meta name="description" content="{p['seoDescription']}">
    <meta name="keywords" content="{p['name']}, khóa vân tay adel, khóa điện tử adel, livo deco, nhà phân phối khóa adel livo deco, {p.get('categoryName', 'khóa thông minh')}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://livodeco.vn/san-pham/{p['slug']}.html">
    <meta property="og:type" content="product">
    <meta property="og:site_name" content="Livo Deco - ADEL Official Vietnam">
    <meta property="og:title" content="{p['seoTitle']}">
    <meta property="og:description" content="{p['seoDescription']}">
    <meta property="og:url" content="https://livodeco.vn/san-pham/{p['slug']}.html">
    <meta property="og:image" content="https://livodeco.vn/{p['image']}">
    <script type="application/ld+json">{schema_json_str}</script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .seo-prose h2, .seo-prose h3 {{
            color: #1e3a8a;
            font-weight: 800;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }}
        .seo-prose p {{
            margin-bottom: 0.85rem;
            line-height: 1.8;
            color: #334155;
        }}
        .seo-prose ul {{
            list-style-type: disc;
            padding-left: 1.5rem;
            margin-bottom: 1.25rem;
            color: #334155;
        }}
        .seo-prose li {{
            margin-bottom: 0.45rem;
            line-height: 1.7;
        }}
        .onpage-link {{
            color: #1d4ed8;
            font-weight: 600;
            text-decoration: underline;
            text-underline-offset: 3px;
        }}
        .onpage-link:hover {{
            color: #1e3a8a;
        }}
        details > summary::-webkit-details-marker {{
            display: none;
        }}
        /* High-Gloss Metallic Light Sweep Glint */
        .light-sweep-container {{
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .light-sweep-container::after {{
            content: '';
            position: absolute;
            top: -60%;
            left: -130%;
            width: 60%;
            height: 220%;
            background: linear-gradient(
                105deg,
                transparent 0%,
                rgba(255, 255, 255, 0.05) 30%,
                rgba(255, 255, 255, 0.75) 48%,
                rgba(255, 255, 255, 1.0) 52%,
                rgba(255, 255, 255, 0.75) 56%,
                transparent 75%,
                transparent 100%
            );
            transform: skewX(-22deg);
            pointer-events: none;
            opacity: 0;
            z-index: 20;
            mix-blend-mode: screen;
        }}
        .group:hover .light-sweep-container::after,
        .light-sweep-container:hover::after {{
            opacity: 1;
            animation: light-sweep-glint 0.85s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }}
        @keyframes light-sweep-glint {{
            0% {{ left: -130%; opacity: 0; }}
            15% {{ opacity: 1; }}
            85% {{ opacity: 1; }}
            100% {{ left: 170%; opacity: 0; }}
        }}

        /* RIGHT-CENTER FLOATING CONTACT DOCK & SOCIAL ANIMATION */
        @keyframes phone-ring {{
            0%, 100% {{ transform: rotate(0deg) scale(1); }}
            10%, 30% {{ transform: rotate(-16deg) scale(1.08); }}
            20%, 40% {{ transform: rotate(16deg) scale(1.08); }}
            50% {{ transform: rotate(0deg) scale(1); }}
        }}
        @keyframes zalo-heartbeat {{
            0%, 100% {{ transform: scale(1); }}
            15% {{ transform: scale(1.12); }}
            30% {{ transform: scale(1); }}
            45% {{ transform: scale(1.08); }}
            60% {{ transform: scale(1); }}
        }}
        @keyframes mess-bounce {{
            0%, 100% {{ transform: translateY(0) scale(1); }}
            20% {{ transform: translateY(-6px) scale(1.06); }}
            40% {{ transform: translateY(2px) scale(0.98); }}
            60% {{ transform: translateY(-3px) scale(1.02); }}
            80% {{ transform: translateY(0) scale(1); }}
        }}
        @keyframes pulse-wave-emerald {{
            0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.75); }}
            70% {{ transform: scale(1); box-shadow: 0 0 0 14px rgba(16, 185, 129, 0); }}
            100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
        }}
        @keyframes pulse-wave-blue {{
            0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.75); }}
            70% {{ transform: scale(1); box-shadow: 0 0 0 14px rgba(37, 99, 235, 0); }}
            100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(37, 99, 235, 0); }}
        }}
        @keyframes pulse-wave-purple {{
            0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(168, 85, 247, 0.75); }}
            70% {{ transform: scale(1); box-shadow: 0 0 0 14px rgba(168, 85, 247, 0); }}
            100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(168, 85, 247, 0); }}
        }}
        .anim-phone-ring {{
            animation: phone-ring 2.8s ease-in-out infinite, pulse-wave-emerald 2.2s infinite;
        }}
        .anim-zalo-beat {{
            animation: zalo-heartbeat 2.6s ease-in-out infinite, pulse-wave-blue 2.2s infinite 0.6s;
        }}
        .anim-mess-bounce {{
            animation: mess-bounce 3s ease-in-out infinite, pulse-wave-purple 2.2s infinite 1.2s;
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased selection:bg-blue-600 selection:text-white">

    <!-- Topbar -->
    <header class="bg-slate-950 text-slate-300 text-xs py-2 border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <span class="text-emerald-400 font-bold flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                    Nhà Phân Phối Chính Thức ADEL Việt Nam - Livo Deco
                </span>
                <span class="hidden md:inline text-slate-600">|</span>
                <span class="hidden md:inline"><i class="fa-solid fa-certificate text-amber-400 mr-1"></i> CO/CQ Chính Hãng 100%</span>
            </div>
            <div class="flex items-center gap-4">
                <a href="tel:0903354397" class="text-white font-bold hover:text-blue-400 transition"><i class="fa-solid fa-phone text-blue-500 mr-1"></i> Hotline: 0903 354 397</a>
            </div>
        </div>
    </header>

    <!-- Main Navigation Bar -->
    <nav class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
            <a href="../index.html" class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-900 to-blue-600 flex items-center justify-center text-white shadow-md">
                    <i class="fa-solid fa-fingerprint text-xl"></i>
                </div>
                <div>
                    <div class="text-2xl font-black tracking-tight text-blue-950 flex items-center gap-1">
                        LIVO DECO
                        <span class="text-[10px] uppercase font-bold px-1.5 py-0.5 rounded bg-blue-100 text-blue-800">ADEL Official</span>
                    </div>
                    <p class="text-[10px] font-semibold text-slate-500 uppercase tracking-widest">Smart Lock & Luxury Living</p>
                </div>
            </a>

            <div class="hidden md:flex items-center space-x-1 text-xs font-bold text-slate-700">
                <a href="../index.html" class="px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-600 transition">Trang Chủ</a>
                <a href="../index.html#products-section" class="px-3 py-2 rounded-lg bg-blue-50 text-blue-600 transition">Khóa Điện Tử ADEL</a>
                <a href="../index.html#products-section" class="px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-600 transition">Thiết Bị Vệ Sinh</a>
                <a href="../index.html#products-section" class="px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-600 transition">Nội Thất Cao Cấp</a>
                <a href="../tin-tuc.html" class="px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-600 transition">Tin Tức & Cẩm Nang</a>
                <a href="../chinh-sach-bao-hanh.html" class="px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-600 transition">Bảo Hành 24T</a>
            </div>

            <div class="flex items-center gap-3">
                <a href="tel:0903354397" class="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs shadow-md transition flex items-center gap-2">
                    <i class="fa-solid fa-phone"></i>
                    <span>Tư Vấn: 0903 354 397</span>
                </a>
            </div>
        </div>
    </nav>

    <!-- Breadcrumb -->
    <div class="bg-slate-100 border-b border-slate-200 py-3">
        <div class="max-w-7xl mx-auto px-4 flex items-center space-x-2 text-xs font-semibold text-slate-500">
            <a href="../index.html" class="hover:text-blue-600"><i class="fa-solid fa-house mr-1"></i> Trang chủ</a>
            <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
            <a href="../index.html#products-section" class="hover:text-blue-600">{p.get('categoryName', 'Khóa ADEL')}</a>
            <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
            <span class="text-slate-900 font-bold truncate max-w-sm">{p['name']}</span>
        </div>
    </div>

    <!-- Product Showcase -->
    <main class="max-w-7xl mx-auto px-4 py-10">
        <!-- ROW 1: Original Product Photo (Left) + Buying Info & Key Features (Right) -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-stretch">
            
            <!-- Top-Left: Clean Original Product Image Card -->
            <div class="lg:col-span-6 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-sm flex flex-col justify-between">
                <div class="flex items-center justify-between">
                    <span class="text-[11px] font-bold text-blue-700 bg-blue-50 border border-blue-100 px-3 py-1 rounded-full uppercase tracking-wider">
                        {p.get('categoryName', 'Khóa Điện Tử ADEL')}
                    </span>
                    <span class="text-xs font-semibold text-slate-400">
                        Mã SP: <strong class="text-slate-700">{p['id'].upper()}</strong>
                    </span>
                </div>

                <div class="relative min-h-[400px] flex-1 flex items-center justify-center p-4 my-2 light-sweep-container group rounded-2xl">
                    <img src="../{p['image']}" alt="{p['name']}" class="max-h-[380px] max-w-full w-auto object-contain transition duration-300 hover:scale-105">
                </div>

                <div class="flex items-center justify-between text-xs text-slate-500 pt-3 border-t border-slate-100">
                    <span><i class="fa-solid fa-circle-check text-emerald-500 mr-1"></i> Hàng chính hãng ADEL 100%</span>
                    <span><i class="fa-solid fa-shield-halved text-blue-600 mr-1"></i> Đầy đủ chứng nhận CO/CQ</span>
                </div>
            </div>

            <!-- Top-Right: Product Information, Features & CTA Buttons -->
            <div class="lg:col-span-6 flex flex-col justify-between space-y-5">
                <div>
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-xs font-bold uppercase tracking-wider mb-2">
                        {p.get('badge', 'Chính Hãng ADEL')}
                    </div>
                    <h1 class="text-2xl sm:text-3xl font-black text-slate-900 leading-tight">{p['name']}</h1>
                    <div class="mt-3 flex items-baseline gap-4">
                        <span class="text-3xl font-black text-blue-700">{p['price']}</span>
                        <span class="text-xs font-bold text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-md border border-emerald-200">
                            <i class="fa-solid fa-check"></i> Sẵn hàng tại tổng kho Livo Deco
                        </span>
                    </div>
                </div>

                <!-- Features Highlight -->
                <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm flex-1 flex flex-col justify-center">
                    <h2 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-3 flex items-center gap-2">
                        <i class="fa-solid fa-star text-amber-500"></i> Tính Năng Nổi Bật Chính Hãng
                    </h2>
                    <ul class="text-xs text-slate-600 leading-relaxed space-y-1">
                        {features_li}
                    </ul>
                </div>

                <!-- Call to Action Buttons -->
                <div class="space-y-3 pt-1">
                    <div class="grid grid-cols-2 gap-3">
                        <a href="tel:0903354397" class="py-3.5 px-4 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-sm shadow-lg shadow-blue-600/30 transition flex items-center justify-center gap-2 text-center">
                            <i class="fa-solid fa-phone"></i> Gọi Khảo Sát & Lắp Ngay
                        </a>
                        <a href="https://zalo.me/0903354397" target="_blank" class="py-3.5 px-4 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-sm transition flex items-center justify-center gap-2 text-center">
                            <i class="fa-solid fa-comment-dots text-blue-400"></i> Chat Zalo Nhận Báo Giá
                        </a>
                    </div>
                    <div class="grid grid-cols-3 gap-2 text-center text-[11px] text-slate-500 pt-2 border-t border-slate-200">
                        <div><i class="fa-solid fa-truck-fast text-blue-600 mr-1"></i> Giao siêu tốc 2h</div>
                        <div><i class="fa-solid fa-tools text-blue-600 mr-1"></i> Lắp đặt tận nơi</div>
                        <div><i class="fa-solid fa-clock-rotate-left text-blue-600 mr-1"></i> Bảo hành 24T</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ROW 2: Specifications Table (Bottom-Left) + Visual Feature Infographic (Bottom-Right) -->
        <div class="mt-8 grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-stretch">
            <!-- Bottom-Left: Specifications Table -->
            <div class="lg:col-span-6 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm">
                <h2 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-sliders text-blue-600"></i> Thông Số Kỹ Thuật Chi Tiết
                </h2>
                <table class="w-full text-xs">
                    <tbody>
                        {specs_tr}
                    </tbody>
                </table>
            </div>

            <!-- Bottom-Right: Official Product Feature & Visual Diagram -->
            <div class="lg:col-span-6 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm flex flex-col items-center justify-between">
                <h2 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-4 flex items-center gap-2 self-start w-full border-b border-slate-100 pb-3">
                    <i class="fa-solid fa-image text-blue-600"></i> {right_box_title}
                </h2>
                <div class="flex-1 flex flex-col items-center justify-center w-full gap-4">
                    {infographic_imgs}
                </div>
            </div>
        </div>

        <!-- ROW 3: Natural Product Description & Review + FAQ -->
        <section class="mt-12 bg-white rounded-3xl border border-slate-200 p-8 sm:p-12 shadow-sm">
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 mb-6 pb-4 border-b border-slate-200">
                Mô Tả &amp; Đánh Giá Chi Tiết {eval_heading_name}
            </h2>
            
            <div class="seo-prose text-sm">
                <h3>1. Thiết kế tổng quan và xuất xứ chính hãng ADEL</h3>
                <p>
                    <strong>{p['name']}</strong> là mẫu khóa thông minh thuộc dòng <a href="../index.html#products-section" class="onpage-link">{p.get('categoryName', 'Khóa Điện Tử ADEL')}</a> của tập đoàn công nghệ <strong>ADEL</strong> (thương hiệu khóa vân tay tiên phong theo tiêu chuẩn Hoa Kỳ từ năm 1993), hiện được phân phối chính thức tại Việt Nam bởi <strong><a href="../index.html" class="onpage-link">Livo Deco</a></strong> với mức giá niêm yết <strong>{p['price']}</strong>.
                </p>
                <p>
                    Sở hữu ngoại quan tinh tế với tông màu <strong>{color}</strong> sang trọng, sản phẩm đáp ứng đồng thời yêu cầu khắt khe về thẩm mỹ kiến trúc nội thất và tiêu chuẩn an ninh cao cấp cho căn hộ chung cư, biệt thự, nhà phố cũng như văn phòng hiện đại.
                </p>

                <h3>2. Công nghệ bảo mật sinh trắc học &amp; Độ bền vật liệu</h3>
                <p>
                    Toàn bộ phần thân và vỏ khóa <strong>{p['name']}</strong> được chế tác từ <strong>{material}</strong>, bề mặt xử lý chống trầy xước và chống oxy hóa, thích nghi hoàn hảo với điều kiện khí hậu nóng ẩm tại Việt Nam.
                </p>
                <ul>
                    <li><strong>Phương thức mở khóa linh hoạt:</strong> Tích hợp {unlock_methods}, giúp người dùng thao tác mở cửa nhanh chóng và tiện lợi.</li>
                    <li><strong>Nhận diện vân tay siêu nhạy:</strong> Đầu đọc vân tay sinh trắc học cho tốc độ phản hồi dưới 0.5 giây, ngăn chặn hoàn toàn vân tay giả mạo bằng silicon hay hình ảnh.</li>
                    <li><strong>Dung lượng bộ nhớ lớn:</strong> Hỗ trợ lưu trữ {capacity}, dễ dàng đăng ký hoặc xóa từng người dùng trực tiếp trên khóa.</li>
                    <li><strong>An toàn chủ động:</strong> Tích hợp mã số ảo chống nhìn trộm, tự động khóa bàn phím khi nhập sai mật khẩu 5 lần liên tiếp và phát âm thanh cảnh báo khi có ngoại lực cạy phá.</li>
                    <li><strong>Nguồn điện bền bỉ:</strong> Vận hành bằng {power_supply}, có cảnh báo pin yếu sớm trước 2–3 tuần và trang bị cổng cấp nguồn dự phòng khẩn cấp bên ngoài.</li>
                </ul>

                <h3>3. Tiêu chuẩn đố cửa &amp; Khảo sát lắp đặt thực tế</h3>
                <p>
                    Mẫu khóa <strong>{p['name']}</strong> tương thích tốt với các loại cửa có độ dày <strong>{door_thickness}</strong>. Để chọn đúng kích thước cơ khóa cho từng chất liệu cửa, quý khách có thể xem thêm bài hướng dẫn <a href="../tin-tuc/huong-dan-chon-khoa-van-tay-phu-hop-voi-do-day-va-chat-lieu-cua.html" class="onpage-link">tiêu chuẩn đố cửa gỗ, nhôm Xingfa và cửa sắt khi lắp khóa điện tử</a>, hoặc tham khảo thêm các mẫu cùng phân khúc như <a href="{sib1['slug']}.html" class="onpage-link">{sib1['name']}</a> ({sib1['price']}), <a href="{sib2['slug']}.html" class="onpage-link">{sib2['name']}</a> ({sib2['price']}) và <a href="{sib3['slug']}.html" class="onpage-link">{sib3['name']}</a> ({sib3['price']}).
                </p>

                <h3>4. Chính sách bảo hành &amp; Lắp đặt tận nơi của Livo Deco</h3>
                <ul>
                    <li><strong>Bảo hành chính hãng 24 tháng:</strong> Áp dụng <a href="../chinh-sach-bao-hanh.html" class="onpage-link">chính sách bảo hành 24 tháng tận nơi</a>, đổi mới 1 đổi 1 trong 30 ngày đầu nếu phát sinh lỗi kỹ thuật từ nhà sản xuất.</li>
                    <li><strong>Khảo sát &amp; Lắp đặt tận nhà:</strong> Đội ngũ kỹ thuật viên theo <a href="../chinh-sach-lap-dat.html" class="onpage-link">quy trình lắp đặt chuẩn hãng của Livo Deco</a> hỗ trợ khảo sát đố cửa miễn phí và lắp đặt nhanh trong 2 giờ tại TP.HCM, Hà Nội, Đà Nẵng cùng hệ thống đại lý toàn quốc.</li>
                    <li><strong>Chứng nhận CO/CQ &amp; Thanh toán linh hoạt:</strong> Cung cấp đầy đủ hồ sơ CO/CQ, hóa đơn VAT cho dự án và hỗ trợ <a href="../chinh-sach-thanh-toan.html" class="onpage-link">kiểm tra nghiệm thu khóa tại nhà trước khi thanh toán (COD)</a>.</li>
                </ul>
            </div>

            <!-- Clean FAQ Section -->
            <div class="mt-10 pt-8 border-t border-slate-200">
                <h3 class="text-lg sm:text-xl font-black text-slate-900 mb-5">
                    Câu Hỏi Thường Gặp Về {p['name']}
                </h3>
                <div class="space-y-3">
                    {faq_items_html}
                </div>
            </div>
        </section>

        <!-- Related Products Section -->
        <div class="mt-16">
            <div class="flex items-center justify-between mb-6">
                <h2 class="text-lg font-black text-slate-900">Sản Phẩm Cùng Phân Khúc Tại Livo Deco</h2>
                <a href="../index.html#products-section" class="text-xs font-bold text-blue-600 hover:underline">Xem tất cả 81+ mẫu &rarr;</a>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
                {related_cards}
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-950 text-slate-400 text-xs border-t border-slate-800 py-10 mt-16">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row justify-between items-center gap-4">
            <div>
                <p class="font-bold text-white text-sm">LIVO DECO - NHÀ PHÂN PHỐI CHÍNH THỨC KHÓA ADEL &amp; NỘI THẤT CAO CẤP</p>
                <p class="text-slate-500 mt-1">Hotline: 0903 354 397 | Email: kinhdoanh@livodeco.vn | Website: https://livodeco.vn</p>
            </div>
            <p>© 2026 Livo Deco Official. All rights reserved.</p>
        </div>
    </footer>

    <!-- STICKY FLOATING CONTACT DOCK (Hotline, Zalo, Messenger, Scroll-to-Top) -->
    <div class="fixed right-3 md:right-5 top-1/2 -translate-y-1/2 z-50 flex flex-col items-center gap-3">
        <!-- Hotline -->
        <a href="tel:0903354397" aria-label="Hotline Tư Vấn" class="w-12 h-12 md:w-13 md:h-13 rounded-full bg-gradient-to-tr from-emerald-600 to-emerald-400 text-white shadow-lg shadow-emerald-500/30 flex items-center justify-center transition-all duration-300 hover:scale-115 group relative anim-phone-ring">
            <i class="fa-solid fa-phone text-lg"></i>
            <span class="absolute right-[calc(100%+12px)] top-1/2 -translate-y-1/2 bg-slate-900/95 backdrop-blur text-white text-xs font-semibold px-3 py-1.5 rounded-xl shadow-xl whitespace-nowrap opacity-0 group-hover:opacity-100 transition-all duration-200 pointer-events-none border border-slate-700/60 flex items-center gap-1.5">
                <i class="fa-solid fa-phone-volume text-emerald-400"></i> Hotline: 0903 354 397
            </span>
        </a>

        <!-- Zalo -->
        <a href="https://zalo.me/0903354397" target="_blank" rel="noopener noreferrer" aria-label="Chat Zalo" class="w-12 h-12 md:w-13 md:h-13 rounded-full bg-gradient-to-tr from-blue-700 to-blue-500 text-white shadow-lg shadow-blue-500/30 flex items-center justify-center transition-all duration-300 hover:scale-115 group relative anim-zalo-beat">
            <span class="font-black text-xs tracking-tight">ZALO</span>
            <span class="absolute right-[calc(100%+12px)] top-1/2 -translate-y-1/2 bg-slate-900/95 backdrop-blur text-white text-xs font-semibold px-3 py-1.5 rounded-xl shadow-xl whitespace-nowrap opacity-0 group-hover:opacity-100 transition-all duration-200 pointer-events-none border border-slate-700/60 flex items-center gap-1.5">
                <i class="fa-solid fa-comment-dots text-blue-400"></i> Chat Zalo Tư Vấn
            </span>
        </a>

        <!-- Messenger -->
        <a href="https://m.me/livodeco" target="_blank" rel="noopener noreferrer" aria-label="Chat Messenger Facebook" class="w-12 h-12 md:w-13 md:h-13 rounded-full bg-gradient-to-tr from-[#00c6ff] via-[#0078ff] to-[#a033ff] text-white shadow-lg shadow-blue-500/30 flex items-center justify-center transition-all duration-300 hover:scale-115 group relative anim-mess-bounce">
            <i class="fa-brands fa-facebook-messenger text-xl"></i>
            <span class="absolute right-[calc(100%+12px)] top-1/2 -translate-y-1/2 bg-slate-900/95 backdrop-blur text-white text-xs font-semibold px-3 py-1.5 rounded-xl shadow-xl whitespace-nowrap opacity-0 group-hover:opacity-100 transition-all duration-200 pointer-events-none border border-slate-700/60 flex items-center gap-1.5">
                <i class="fa-brands fa-facebook-messenger text-[#00c6ff]"></i> Facebook Messenger
            </span>
        </a>

        <!-- Scroll To Top Button -->
        <button id="scrollToTopBtn" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" aria-label="Cuộn lên đầu trang" class="w-11 h-11 md:w-12 md:h-12 rounded-full bg-slate-900/90 hover:bg-blue-600 text-white shadow-lg shadow-slate-900/20 flex items-center justify-center transition-all duration-300 hover:scale-110 opacity-0 pointer-events-none translate-x-3 group relative border border-white/20 mt-1 cursor-pointer">
            <i class="fa-solid fa-arrow-up text-sm"></i>
            <span class="absolute right-[calc(100%+12px)] top-1/2 -translate-y-1/2 bg-slate-900/95 backdrop-blur text-white text-xs font-semibold px-2.5 py-1.5 rounded-xl shadow-xl whitespace-nowrap opacity-0 group-hover:opacity-100 transition-all duration-200 pointer-events-none border border-slate-700/60">
                Lên đầu trang
            </span>
        </button>
    </div>

    <script>
        const scrollTopBtn = document.getElementById('scrollToTopBtn');
        if (scrollTopBtn) {{
            window.addEventListener('scroll', () => {{
                if (window.scrollY > 280) {{
                    scrollTopBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-x-3');
                    scrollTopBtn.classList.add('opacity-100', 'translate-x-0');
                }} else {{
                    scrollTopBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-x-3');
                    scrollTopBtn.classList.remove('opacity-100', 'translate-x-0');
                }}
            }}, {{ passive: true }});
        }}
    </script>
</body>
</html>"""

os.makedirs("san-pham", exist_ok=True)

all_prods = data.get("adel_products", []) + data.get("sanitary_products", []) + data.get("furniture_products", [])

created_count = 0
for p in all_prods:
    slug = p["slug"]
    html_content = generate_product_html(p, all_prods)
    with open(f"san-pham/{slug}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    created_count += 1

print(f"Generated {created_count} clean, natural product pages in 'san-pham/'!")
