import fitz
import cv2
import numpy as np
import os

doc = fitz.open('YALE CATALOGUE 2025.pdf')
os.makedirs('images/products_png', exist_ok=True)

tasks = [
    {
        'slug': 'khoa-dien-tu-yale-luna-pro',
        'page': 17, # P18
        'crop': (0.70, 0.16, 0.98, 0.48),
        'min_area': 15000,
        'pad': 10
    },
    {
        'slug': 'khoa-dien-tu-yale-kyra-pro',
        'page': 18, # P19
        'crop': (0.65, 0.18, 0.96, 0.48),
        'min_area': 15000,
        'pad': 10
    },
    {
        'slug': 'khoa-dien-tu-yale-ydm7116a',
        'page': 19, # P20
        'crop': (0.70, 0.18, 0.95, 0.48),
        'min_area': 15000,
        'pad': 10
    },
    {
        'slug': 'khoa-dien-tu-yale-ydm4109a',
        'page': 20, # P21
        'crop': (0.70, 0.16, 0.95, 0.46),
        'min_area': 15000,
        'pad': 10
    },
    {
        'slug': 'khoa-dien-tu-yale-zuri',
        'page': 21, # P22
        'crop': (0.65, 0.18, 0.95, 0.48),
        'min_area': 15000,
        'pad': 10
    },
    {
        'slug': 'khoa-dien-tu-yale-ydma-100np',
        'page': 22, # P23
        'crop': (0.68, 0.18, 0.96, 0.48),
        'min_area': 10000,
        'pad': 10
    },
    {
        'slug': 'khoa-dien-tu-yale-ydme-100-nxt',
        'page': 23, # P24
        'crop': (0.70, 0.16, 0.96, 0.46),
        'min_area': 12000,
        'pad': 10
    },
    {
        'slug': 'khoa-dien-tu-yale-ydme-200-nxt',
        'page': 24, # P25
        'crop': (0.70, 0.16, 0.96, 0.46),
        'min_area': 12000,
        'pad': 10
    },
    {
        'slug': 'khoa-dien-tu-yale-ydd724a',
        'page': 25, # P26
        'crop': (0.70, 0.18, 0.92, 0.46),
        'min_area': 12000,
        'pad': 10
    },
    {
        'slug': 'khoa-dien-tu-yale-ydr413a',
        'page': 26, # P27
        'crop': (0.70, 0.16, 0.90, 0.44),
        'min_area': 12000,
        'pad': 10
    },
    {
        'slug': 'tay-day-hoi-yale-yic-2124',
        'page': 105, # P106
        'crop': (0.12, 0.14, 0.44, 0.42),
        'min_area': 8000,
        'pad': 10
    },
    {
        'slug': 'cau-noi-yale-connect-plus-hub-2-wifi',
        'page': 27, # P28
        'crop': (0.16, 0.35, 0.36, 0.47),
        'min_area': 4000,
        'pad': 10
    },
    {
        'slug': 'module-bluetooth-yale-home',
        'page': 27, # P28
        'crop': (0.64, 0.35, 0.84, 0.47),
        'min_area': 4000,
        'pad': 10
    },
    {
        'slug': 'module-smart-home-yale-zigbee',
        'page': 28, # P29
        'crop': (0.18, 0.64, 0.38, 0.76),
        'min_area': 4000,
        'pad': 10
    },
    {
        'slug': 'module-smart-home-yale-zwave-700',
        'page': 28, # P29
        'crop': (0.18, 0.83, 0.38, 0.95),
        'min_area': 4000,
        'pad': 10
    }
]

for t in tasks:
    slug = t['slug']
    page = doc[t['page']]
    rect = page.rect
    x0_r, y0_r, x1_r, y1_r = t['crop']
    clip_rect = fitz.Rect(rect.width * x0_r, rect.height * y0_r, rect.width * x1_r, rect.height * y1_r)
    pix = page.get_pixmap(dpi=250, clip=clip_rect)
    
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    if pix.n == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    elif pix.n == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
    h, w = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    mask = np.zeros((h + 2, w + 2), np.uint8)
    for seed in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1)]:
        if gray[seed[1], seed[0]] > 220:
            cv2.floodFill(gray.copy(), mask, seed, 0, loDiff=25, upDiff=25, flags=cv2.FLOODFILL_MASK_ONLY | (255 << 8))
            
    bg_mask = mask[1:h+1, 1:w+1] == 255
    fg_mask = (~bg_mask).astype(np.uint8) * 255
    
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(fg_mask)
    obj_mask = np.zeros_like(fg_mask)
    
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area >= t['min_area']:
            obj_mask[labels == i] = 255
            
    if np.sum(obj_mask) == 0:
        obj_mask = fg_mask
        
    y_idx, x_idx = np.where(obj_mask == 255)
    if len(y_idx) > 0:
        y0, y1 = y_idx.min(), y_idx.max()
        x0, x1 = x_idx.min(), x_idx.max()
        pad = t['pad']
        y0 = max(0, y0 - pad)
        y1 = min(h, y1 + pad)
        x0 = max(0, x0 - pad)
        x1 = min(w, x1 + pad)
        
        cropped = img[y0:y1+1, x0:x1+1]
        alpha = obj_mask[y0:y1+1, x0:x1+1]
        rgba = cv2.cvtColor(cropped, cv2.COLOR_BGR2BGRA)
        rgba[:, :, 3] = alpha
        
        out_path = f"images/products_png/{slug}.png"
        cv2.imwrite(out_path, rgba)
        print(f"Successfully generated: {out_path} ({rgba.shape[1]}x{rgba.shape[0]})")
    else:
        print(f"Failed to crop: {slug}")
