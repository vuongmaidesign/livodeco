import json
import re
import unicodedata

def slugify(text):
    text = unicodedata.normalize('NFD', text)
    text = re.sub(r'[\u0300-\u036f]', '', text)
    text = text.replace('đ', 'd').replace('Đ', 'd')
    text = re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-').lower()
    return text

with open("products_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data.get("adel_products", []):
    item["slug"] = slugify(item["name"])

for item in data.get("sanitary_products", []):
    item["slug"] = slugify(item["name"])

for item in data.get("furniture_products", []):
    item["slug"] = slugify(item["name"])

with open("products_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Slugify updated successfully! Sample slug:", data["adel_products"][0]["slug"])
