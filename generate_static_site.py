import json
import os
import re

with open("news_and_policies.json", "r", encoding="utf-8") as f:
    site_data = json.load(f)

news_articles = site_data.get("news", [])
policies = site_data.get("policies", {})

def format_bold(text):
    return re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)

COMMON_ORG_SCHEMA = {
    "@type": "Organization",
    "@id": "https://livodeco.vn/#organization",
    "name": "Livo Deco",
    "legalName": "Hệ Thống Phân Phối Khóa Điện Tử ADEL & Nội Thất Livo Deco",
    "url": "https://livodeco.vn/",
    "telephone": "+84903354397",
    "email": "kinhdoanh@livodeco.vn",
    "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+84-903-354-397",
        "contactType": "customer service",
        "areaServed": "VN",
        "availableLanguage": ["Vietnamese"]
    }
}

COMMON_LOCAL_BUSINESS_SCHEMA = {
    "@type": "LocalBusiness",
    "@id": "https://livodeco.vn/#localbusiness",
    "name": "Livo Deco - Nhà Phân Phối Khóa Điện Tử ADEL & Nội Thất Cao Cấp",
    "url": "https://livodeco.vn/",
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

# 1. Generate Policy Pages with Full Schema.org JSON-LD
for key, pol in policies.items():
    slug = pol["slug"]
    title = pol["title"]
    content_raw = pol["content"].strip().split("\n")
    
    html_paragraphs = []
    in_ul = False
    for line in content_raw:
        line = line.strip()
        if not line:
            if in_ul:
                html_paragraphs.append("</ul>")
                in_ul = False
            continue
        if line.startswith("### "):
            if in_ul:
                html_paragraphs.append("</ul>")
                in_ul = False
            html_paragraphs.append(f"<h2 class='text-xl font-bold text-blue-900 mt-6 mb-3'>{line.replace('### ', '')}</h2>")
        elif line.startswith("#### "):
            if in_ul:
                html_paragraphs.append("</ul>")
                in_ul = False
            html_paragraphs.append(f"<h3 class='text-lg font-bold text-slate-800 mt-4 mb-2'>{line.replace('#### ', '')}</h3>")
        elif line.startswith("- "):
            if not in_ul:
                html_paragraphs.append("<ul class='list-disc pl-5 space-y-2 mb-4 text-slate-700'>")
                in_ul = True
            item_text = format_bold(line.replace("- ", ""))
            html_paragraphs.append(f"<li>{item_text}</li>")
        else:
            if in_ul:
                html_paragraphs.append("</ul>")
                in_ul = False
            p_text = format_bold(line)
            html_paragraphs.append(f"<p class='text-slate-700 leading-relaxed mb-3'>{p_text}</p>")
    if in_ul:
        html_paragraphs.append("</ul>")
    
    body_html = "\n".join(html_paragraphs)

    policy_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"https://livodeco.vn/{slug}.html#webpage",
                "url": f"https://livodeco.vn/{slug}.html",
                "name": f"{title} - Livo Deco Nhà Phân Phối ADEL Chính Hãng",
                "description": f"{title} tại Livo Deco - Nhà phân phối chính thức thương hiệu khóa điện tử ADEL & Nội thất cao cấp tại Việt Nam.",
                "inLanguage": "vi",
                "isPartOf": {"@id": "https://livodeco.vn/#website"},
                "about": {"@id": "https://livodeco.vn/#organization"}
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
                        "name": title,
                        "item": f"https://livodeco.vn/{slug}.html"
                    }
                ]
            },
            COMMON_ORG_SCHEMA,
            COMMON_LOCAL_BUSINESS_SCHEMA
        ]
    }
    policy_schema_str = json.dumps(policy_schema, ensure_ascii=False)

    page_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Livo Deco Nhà Phân Phối ADEL Chính Hãng</title>
    <meta name="description" content="{title} tại Livo Deco - Nhà phân phối chính thức thương hiệu khóa điện tử ADEL & Nội thất cao cấp tại Việt Nam.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://livodeco.vn/{slug}.html">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Livo Deco - ADEL Official Vietnam">
    <meta property="og:title" content="{title} - Livo Deco">
    <meta property="og:description" content="{title} tại Livo Deco - Nhà phân phối chính thức thương hiệu khóa điện tử ADEL & Nội thất cao cấp tại Việt Nam.">
    <meta property="og:url" content="https://livodeco.vn/{slug}.html">
    <script type="application/ld+json">{policy_schema_str}</script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}</style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased">
    <!-- Topbar -->
    <header class="bg-slate-950 text-slate-300 text-xs py-2 border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 flex justify-between items-center">
            <span class="text-emerald-400 font-bold flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                Livo Deco - Nhà Phân Phối Chính Thức ADEL Việt Nam
            </span>
            <a href="tel:0903354397" class="text-white font-bold hover:text-blue-400"><i class="fa-solid fa-phone text-blue-500 mr-1"></i> Hotline: 0903 354 397</a>
        </div>
    </header>

    <!-- Nav -->
    <nav class="sticky top-0 z-40 bg-white/95 backdrop-blur border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center text-white font-black">
                    <i class="fa-solid fa-fingerprint text-xl"></i>
                </div>
                <div>
                    <div class="text-2xl font-black text-blue-950">LIVO DECO</div>
                    <p class="text-[10px] font-semibold text-slate-500 uppercase tracking-widest">Smart Lock & Luxury Living</p>
                </div>
            </a>
            <div class="flex items-center space-x-4 text-xs font-bold text-slate-700">
                <a href="index.html" class="hover:text-blue-600">Trang Chủ</a>
                <a href="index.html#products-section" class="hover:text-blue-600">Khóa ADEL</a>
                <a href="tin-tuc.html" class="hover:text-blue-600">Tin Tức</a>
                <a href="chinh-sach-bao-hanh.html" class="{'text-blue-600 font-black' if key=='bao-hanh' else 'hover:text-blue-600'}">Bảo Hành</a>
                <a href="chinh-sach-lap-dat.html" class="{'text-blue-600 font-black' if key=='lap-dat' else 'hover:text-blue-600'}">Lắp Đặt</a>
                <a href="chinh-sach-thanh-toan.html" class="{'text-blue-600 font-black' if key=='thanh-toan' else 'hover:text-blue-600'}">Thanh Toán</a>
            </div>
        </div>
    </nav>

    <!-- Content -->
    <main class="max-w-4xl mx-auto px-4 py-12">
        <nav class="text-xs text-slate-500 mb-6 flex items-center gap-2">
            <a href="index.html" class="hover:text-blue-600">Trang chủ</a>
            <i class="fa-solid fa-chevron-right text-[10px]"></i>
            <span class="text-slate-900 font-bold">{title}</span>
        </nav>
        <article class="bg-white rounded-3xl p-8 sm:p-12 border border-slate-200 shadow-sm">
            <div class="flex gap-2 pb-6 border-b border-slate-200 overflow-x-auto text-xs font-bold mb-6">
                <a href="chinh-sach-bao-hanh.html" class="px-4 py-2 rounded-xl transition {'bg-blue-600 text-white' if key=='bao-hanh' else 'bg-slate-100 text-slate-700 hover:bg-blue-50'}">Chính Sách Bảo Hành</a>
                <a href="chinh-sach-lap-dat.html" class="px-4 py-2 rounded-xl transition {'bg-blue-600 text-white' if key=='lap-dat' else 'bg-slate-100 text-slate-700 hover:bg-blue-50'}">Khảo Sát & Lắp Đặt</a>
                <a href="chinh-sach-thanh-toan.html" class="px-4 py-2 rounded-xl transition {'bg-blue-600 text-white' if key=='thanh-toan' else 'bg-slate-100 text-slate-700 hover:bg-blue-50'}">Thanh Toán & Giao Hàng</a>
            </div>
            <h1 class="text-2xl sm:text-3xl font-black text-slate-900 mb-6">{title}</h1>
            <div class="prose max-w-none text-sm">
                {body_html}
            </div>
            <div class="mt-10 p-6 bg-blue-50 border border-blue-200 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <h4 class="font-bold text-blue-950 text-sm">Cần hỗ trợ kỹ thuật hoặc bảo hành tận nơi?</h4>
                    <p class="text-xs text-slate-600 mt-1">Kỹ thuật viên Livo Deco luôn sẵn sàng giải đáp 24/7.</p>
                </div>
                <a href="tel:0903354397" class="px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs shrink-0 transition flex items-center gap-2">
                    <i class="fa-solid fa-phone"></i> 0903 354 397
                </a>
            </div>
        </article>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 text-xs py-8 mt-16 text-center border-t border-slate-800">
        <p>© 2026 LIVO DECO. Nhà Phân Phối Khóa Điện Tử Thông Minh ADEL & Nội Thất Chính Hãng.</p>
    </footer>
</body>
</html>
"""
    with open(f"{slug}.html", "w", encoding="utf-8") as f_out:
        f_out.write(page_html)
    print(f"Generated {slug}.html with Schema.org JSON-LD")

# 2. Generate News Index Page with CollectionPage + Blog + BreadcrumbList Schema
news_cards = "".join([f"""
    <a href="tin-tuc/{n['slug']}.html" class="bg-white rounded-3xl border border-slate-200 overflow-hidden hover:shadow-xl transition group flex flex-col">
        <div class="h-48 overflow-hidden bg-slate-100 relative">
            <img src="{n['image']}" alt="{n['title']}" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <span class="absolute top-3 left-3 text-[10px] font-bold uppercase tracking-wider bg-blue-600 text-white px-2.5 py-1 rounded-md shadow">{n['category']}</span>
        </div>
        <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
                <span class="text-xs text-slate-400">{n['date']} • {n['author']}</span>
                <h3 class="text-base font-extrabold text-slate-900 group-hover:text-blue-600 line-clamp-2 mt-2 leading-snug">{n['title']}</h3>
                <p class="text-xs text-slate-500 line-clamp-3 mt-2 leading-relaxed">{n['excerpt']}</p>
            </div>
            <div class="mt-4 pt-4 border-t border-slate-100 flex items-center text-xs font-bold text-blue-600 group-hover:translate-x-1 transition">
                <span>Xem bài viết chi tiết</span> <i class="fa-solid fa-arrow-right ml-1 text-[10px]"></i>
            </div>
        </div>
    </a>
""" for n in news_articles])

news_index_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "CollectionPage",
            "@id": "https://livodeco.vn/tin-tuc.html#collectionpage",
            "url": "https://livodeco.vn/tin-tuc.html",
            "name": "Tin Tức Khóa Cửa ADEL & Cẩm Nang Nội Thất - Livo Deco",
            "description": "Chuyên mục tin tức, kinh nghiệm chọn mua và lắp đặt khóa điện tử thông minh ADEL, bàn ghế nội thất và thiết bị vệ sinh từ chuyên gia Livo Deco.",
            "inLanguage": "vi",
            "isPartOf": {"@id": "https://livodeco.vn/#website"},
            "mainEntity": {
                "@type": "ItemList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": idx + 1,
                        "url": f"https://livodeco.vn/tin-tuc/{n['slug']}.html",
                        "name": n["title"]
                    }
                    for idx, n in enumerate(news_articles)
                ]
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
                    "name": "Tin Tức & Cẩm Nang Kỹ Thuật",
                    "item": "https://livodeco.vn/tin-tuc.html"
                }
            ]
        },
        COMMON_ORG_SCHEMA,
        COMMON_LOCAL_BUSINESS_SCHEMA
    ]
}
news_index_schema_str = json.dumps(news_index_schema, ensure_ascii=False)

news_index_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tin Tức Khóa Cửa ADEL & Cẩm Nang Nội Thất - Livo Deco</title>
    <meta name="description" content="Chuyên mục tin tức, kinh nghiệm chọn mua và lắp đặt khóa điện tử thông minh ADEL, bàn ghế nội thất và thiết bị vệ sinh từ chuyên gia Livo Deco.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://livodeco.vn/tin-tuc.html">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Livo Deco - ADEL Official Vietnam">
    <meta property="og:title" content="Tin Tức Khóa Cửa ADEL & Cẩm Nang Nội Thất - Livo Deco">
    <meta property="og:description" content="Chuyên mục tin tức, kinh nghiệm chọn mua và lắp đặt khóa điện tử thông minh ADEL, bàn ghế nội thất và thiết bị vệ sinh từ chuyên gia Livo Deco.">
    <meta property="og:url" content="https://livodeco.vn/tin-tuc.html">
    <script type="application/ld+json">{news_index_schema_str}</script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}</style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased">
    <!-- Topbar -->
    <header class="bg-slate-950 text-slate-300 text-xs py-2 border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 flex justify-between items-center">
            <span class="text-emerald-400 font-bold flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                Livo Deco - Nhà Phân Phối Chính Thức ADEL Việt Nam
            </span>
            <a href="tel:0903354397" class="text-white font-bold hover:text-blue-400"><i class="fa-solid fa-phone text-blue-500 mr-1"></i> Hotline: 0903 354 397</a>
        </div>
    </header>

    <!-- Nav -->
    <nav class="sticky top-0 z-40 bg-white/95 backdrop-blur border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center text-white font-black">
                    <i class="fa-solid fa-fingerprint text-xl"></i>
                </div>
                <div>
                    <div class="text-2xl font-black text-blue-950">LIVO DECO</div>
                    <p class="text-[10px] font-semibold text-slate-500 uppercase tracking-widest">Smart Lock & Luxury Living</p>
                </div>
            </a>
            <div class="flex items-center space-x-4 text-xs font-bold text-slate-700">
                <a href="index.html" class="hover:text-blue-600">Trang Chủ</a>
                <a href="index.html#products-section" class="hover:text-blue-600">Khóa ADEL</a>
                <a href="tin-tuc.html" class="text-blue-600 font-black">Tin Tức</a>
                <a href="chinh-sach-bao-hanh.html" class="hover:text-blue-600">Chính Sách</a>
            </div>
        </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 py-12">
        <div class="text-center max-w-2xl mx-auto mb-12">
            <span class="text-xs font-bold uppercase tracking-wider text-blue-600 bg-blue-50 px-3 py-1 rounded-md">Cẩm Nang Kỹ Thuật</span>
            <h1 class="text-3xl sm:text-4xl font-black text-slate-900 mt-3">Tin Tức & Kinh Nghiệm Khóa Thông Minh</h1>
            <p class="text-slate-500 text-sm mt-2">Tổng hợp thông tin sản phẩm ADEL, tư vấn lắp đặt và chính sách bảo hành chính hãng từ Livo Deco.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            {news_cards}
        </div>
    </main>

    <footer class="bg-slate-900 text-slate-400 text-xs py-8 mt-16 text-center border-t border-slate-800">
        <p>© 2026 LIVO DECO. Nhà Phân Phối Khóa Điện Tử Thông Minh ADEL & Nội Thất Chính Hãng.</p>
    </footer>
</body>
</html>
"""
with open("tin-tuc.html", "w", encoding="utf-8") as f_out:
    f_out.write(news_index_html)
print("Generated tin-tuc.html with Schema.org JSON-LD")

# 3. Generate News Article Detail Pages with Article + BreadcrumbList + Organization Schema
os.makedirs("tin-tuc", exist_ok=True)

for n in news_articles:
    slug = n["slug"]
    content_raw = n["content"].strip().split("\n")
    html_paragraphs = []
    in_ul = False
    for line in content_raw:
        line = line.strip()
        if not line:
            if in_ul:
                html_paragraphs.append("</ul>")
                in_ul = False
            continue
        if line.startswith("### "):
            if in_ul:
                html_paragraphs.append("</ul>")
                in_ul = False
            html_paragraphs.append(f"<h2 class='text-xl font-bold text-blue-900 mt-6 mb-3'>{line.replace('### ', '')}</h2>")
        elif line.startswith("#### "):
            if in_ul:
                html_paragraphs.append("</ul>")
                in_ul = False
            html_paragraphs.append(f"<h3 class='text-lg font-bold text-slate-800 mt-4 mb-2'>{line.replace('#### ', '')}</h3>")
        elif line.startswith("- ") or (line[0].isdigit() and line[1] == "."):
            if not in_ul:
                html_paragraphs.append("<ul class='list-disc pl-5 space-y-2 mb-4 text-slate-700'>")
                in_ul = True
            text_item = line[2:].strip() if line.startswith("- ") else line[3:].strip()
            text_item = format_bold(text_item)
            html_paragraphs.append(f"<li>{text_item}</li>")
        else:
            if in_ul:
                html_paragraphs.append("</ul>")
                in_ul = False
            p_text = format_bold(line)
            html_paragraphs.append(f"<p class='text-slate-700 leading-relaxed mb-3'>{p_text}</p>")
    if in_ul:
        html_paragraphs.append("</ul>")

    article_body = "\n".join(html_paragraphs)

    # Convert DD/MM/YYYY to YYYY-MM-DD for ISO schema date
    parts = n["date"].split("/")
    iso_date = f"{parts[2]}-{parts[1]}-{parts[0]}" if len(parts) == 3 else "2026-10-12"

    article_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "@id": f"https://livodeco.vn/tin-tuc/{slug}.html#article",
                "mainEntityOfPage": {
                    "@type": "WebPage",
                    "@id": f"https://livodeco.vn/tin-tuc/{slug}.html"
                },
                "headline": n["title"],
                "description": n["excerpt"],
                "image": [n["image"]],
                "datePublished": iso_date,
                "dateModified": iso_date,
                "author": {
                    "@type": "Organization",
                    "name": n["author"],
                    "url": "https://livodeco.vn/"
                },
                "publisher": COMMON_ORG_SCHEMA,
                "inLanguage": "vi"
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
                        "name": "Tin tức",
                        "item": "https://livodeco.vn/tin-tuc.html"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": n["title"],
                        "item": f"https://livodeco.vn/tin-tuc/{slug}.html"
                    }
                ]
            },
            COMMON_ORG_SCHEMA,
            COMMON_LOCAL_BUSINESS_SCHEMA
        ]
    }
    article_schema_str = json.dumps(article_schema, ensure_ascii=False)

    detail_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{n['title']} - Livo Deco</title>
    <meta name="description" content="{n['excerpt']}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://livodeco.vn/tin-tuc/{slug}.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Livo Deco - ADEL Official Vietnam">
    <meta property="og:title" content="{n['title']}">
    <meta property="og:description" content="{n['excerpt']}">
    <meta property="og:url" content="https://livodeco.vn/tin-tuc/{slug}.html">
    <meta property="og:image" content="{n['image']}">
    <script type="application/ld+json">{article_schema_str}</script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}</style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased">
    <!-- Topbar -->
    <header class="bg-slate-950 text-slate-300 text-xs py-2 border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 flex justify-between items-center">
            <span class="text-emerald-400 font-bold flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                Livo Deco - Nhà Phân Phối Chính Thức ADEL Việt Nam
            </span>
            <a href="tel:0903354397" class="text-white font-bold hover:text-blue-400"><i class="fa-solid fa-phone text-blue-500 mr-1"></i> Hotline: 0903 354 397</a>
        </div>
    </header>

    <!-- Nav -->
    <nav class="sticky top-0 z-40 bg-white/95 backdrop-blur border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
            <a href="../index.html" class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center text-white font-black">
                    <i class="fa-solid fa-fingerprint text-xl"></i>
                </div>
                <div>
                    <div class="text-2xl font-black text-blue-950">LIVO DECO</div>
                    <p class="text-[10px] font-semibold text-slate-500 uppercase tracking-widest">Smart Lock & Luxury Living</p>
                </div>
            </a>
            <div class="flex items-center space-x-4 text-xs font-bold text-slate-700">
                <a href="../index.html" class="hover:text-blue-600">Trang Chủ</a>
                <a href="../index.html#products-section" class="hover:text-blue-600">Khóa ADEL</a>
                <a href="../tin-tuc.html" class="text-blue-600 font-black">Tin Tức</a>
                <a href="../chinh-sach-bao-hanh.html" class="hover:text-blue-600">Chính Sách</a>
            </div>
        </div>
    </nav>

    <main class="max-w-4xl mx-auto px-4 py-12">
        <nav class="text-xs text-slate-500 mb-6 flex items-center gap-2">
            <a href="../index.html" class="hover:text-blue-600">Trang chủ</a>
            <i class="fa-solid fa-chevron-right text-[10px]"></i>
            <a href="../tin-tuc.html" class="hover:text-blue-600">Tin tức</a>
            <i class="fa-solid fa-chevron-right text-[10px]"></i>
            <span class="text-slate-900 font-bold truncate max-w-sm">{n['title']}</span>
        </nav>

        <article class="bg-white rounded-3xl p-8 sm:p-12 border border-slate-200 shadow-sm">
            <span class="text-xs font-bold uppercase tracking-wider bg-blue-50 text-blue-700 px-3 py-1 rounded-md">{n['category']}</span>
            <h1 class="text-2xl sm:text-3xl font-black text-slate-900 mt-4 mb-4 leading-tight">{n['title']}</h1>
            <div class="flex items-center gap-4 text-xs text-slate-400 pb-6 border-b border-slate-100">
                <span><i class="fa-regular fa-calendar mr-1"></i> {n['date']}</span>
                <span><i class="fa-solid fa-user-pen mr-1"></i> {n['author']}</span>
            </div>

            <div class="py-6">
                <img src="{n['image']}" alt="{n['title']}" class="w-full max-h-96 object-cover rounded-2xl mb-6 shadow">
                <div class="prose max-w-none text-sm">
                    {article_body}
                </div>
            </div>

            <div class="mt-6 p-6 bg-slate-50 border border-slate-200 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <h4 class="font-bold text-slate-900 text-sm">Cần tư vấn chọn mẫu khóa ADEL phù hợp ngôi nhà?</h4>
                    <p class="text-xs text-slate-500 mt-1">Livo Deco hỗ trợ khảo sát đố cửa miễn phí tận nơi.</p>
                </div>
                <a href="tel:0903354397" class="px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs shrink-0 transition flex items-center gap-2">
                    <i class="fa-solid fa-phone"></i> 0903 354 397
                </a>
            </div>
        </article>
    </main>

    <footer class="bg-slate-900 text-slate-400 text-xs py-8 mt-16 text-center border-t border-slate-800">
        <p>© 2026 LIVO DECO. Nhà Phân Phối Khóa Điện Tử Thông Minh ADEL & Nội Thất Chính Hãng.</p>
    </footer>
</body>
</html>
"""
    with open(f"tin-tuc/{slug}.html", "w", encoding="utf-8") as f_out:
        f_out.write(detail_html)
    print(f"Generated tin-tuc/{slug}.html with Schema.org JSON-LD")
