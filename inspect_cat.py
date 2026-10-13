import urllib.request
import re
import json

base_url = "https://www.adelgroup.vn"
req = urllib.request.Request(base_url + "/khoa-van-tay/", headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

with open("khoa_van_tay.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved khoa_van_tay.html, length:", len(html))
# Let's see some tags
print("Found procon?", "procon" in html)
print("Found class=\"item\"?", "class=\"item\"" in html)
for m in re.finditer(r'<h[23][^>]*>(.*?)</h[23]>', html):
    print("Header:", m.group(1)[:60])
