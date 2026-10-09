import cv2
import numpy as np
from pathlib import Path

DATA = Path("../../week01_image_basics/data")
OUT = Path("../../week01_image_basics/outputs")
OUT.mkdir(parents=True, exist_ok=True)

img = cv2.imread(str(DATA / "road.jpg"))
assert img is not None, "图片没读到，检查路径/中文路径/后缀"

print("shape:", img.shape)
print("dtype:", img.dtype)
print("min/max:", img.min(), img.max())

# resize：自动驾驶里常用，降低算力
resized = cv2.resize(img, (640, 360))
cv2.imwrite(str(OUT / "01_resized.png"), resized)

# BGR -> RGB，matplotlib 常用
rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imwrite(str(OUT / "02_gray.png"), gray)

# 画一个点和一条线，验证 x/y 与 col/row 的关系
canvas = resized.copy()
h, w = canvas.shape[:2]
cv2.circle(canvas, (w // 2, h // 2), 8, (0, 0, 255), -1)  # BGR: 红
cv2.line(canvas, (0, h - 1), (w - 1, h - 1), (0, 255, 0), 2)
cv2.imwrite(str(OUT / "05_draw_xy_check.png"), canvas)