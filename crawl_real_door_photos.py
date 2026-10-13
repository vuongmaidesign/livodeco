import urllib.request
import re

url = 'https://www.adelgroup.vn/khoa-cua-dien-tu/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    links = list(set(re.findall(r'href=["\'](/[^"\']+\.html)["\']', html)))
    print("Found links:", len(links))
    for l in links[:6]:
        if 'khoa' in l:
            p_url = 'https://www.adelgroup.vn' + l
            try:
                p_html = urllib.request.urlopen(urllib.request.Request(p_url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=10).read().decode('utf-8', errors='ignore')
                imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|png|jpeg))["\']', p_html)
                valid = [img for img in imgs if 'images/' in img and not any(x in img for x in ['logo', 'icon', 'banner', 'footer'])]
                print(l, "=>", valid)
            except Exception as err:
                print("Err page:", err)
except Exception as e:
    print("Error:", e)
