import cv2
import numpy as np
from pathlib import Path

DATA = Path("../../week01_image_basics/data")
OUT = Path("../../week01_image_basics/outputs")
OUT.mkdir(parents=True, exist_ok=True)

img = cv2.imread(str(DATA / "road.jpg"))
img = cv2.resize(img, (640, 360))

# 手动均值模糊：理解邻域平均
img_f = img.astype(np.float32)
k = 5
h, w = img.shape[:2]
manual = np.zeros_like(img_f)
offset = k // 2
for y in range(offset, h - offset):
    for x in range(offset, w - offset):
        patch = img_f[y-offset:y+offset+1, x-offset:x+offset+1]
        manual[y, x] = patch.mean(axis=(0, 1))
manual = np.clip(manual, 0, 255).astype(np.uint8)
cv2.imwrite(str(OUT / "03_manual_box_blur.png"), manual)

# OpenCV 高斯模糊
blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imwrite(str(OUT / "03_gaussian_blur.png"), blur)

# Canny 边缘
edges = cv2.Canny(blur, 50, 150)
cv2.imwrite(str(OUT / "04_edges.png"), edges)