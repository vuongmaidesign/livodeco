import urllib.request
import re

url = 'https://www.adelgroup.vn/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    all_imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|png|webp|jpeg))["\']', html, re.I)
    print("Found total images:", len(all_imgs))
    for img in set(all_imgs):
        if any(k in img.lower() for k in ['banner', 'slide', 'qc', 'intro', 'bg', 'home', 'general']):
            print("Banner candidate:", img)
except Exception as e:
    print("Error:", e)
