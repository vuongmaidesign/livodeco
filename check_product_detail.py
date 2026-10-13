import urllib.request
import re

url = "https://www.adelgroup.vn/khoa-van-tay/khoa-dien-tu-us13lb16/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|png|jpeg))["\']', html)
    print("Found images in product page:", len(imgs))
    for i in set(imgs):
        if 'products' in i or 'upload' in i:
            print("Product img:", i)
except Exception as e:
    print("Error:", e)
