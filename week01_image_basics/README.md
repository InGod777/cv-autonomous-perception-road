# Week01 Image Basics

## Goal
Understand how a camera image is represented as a NumPy array, and run basic preprocessing used in perception pipelines.

## Commands
conda activate cv
python week01_image_basics/src/image_basics.py
python week01_image_basics/src/filters_edges.py

## Outputs
- outputs/01_resized.png
- outputs/02_gray.png
- outputs/03_gaussian_blur.png
- outputs/04_edges.png

## Key observations
- OpenCV uses BGR, not RGB.
- Gaussian blur reduces high-frequency noise before edge detection.
- Canny edges are sensitive to threshold choices.

## Failure cases
- uint8 overflow when doing arithmetic.
- Reading image with Chinese path may fail on some systems.
- (x, y) drawing coordinates are (col, row), while array indexing is [row, col].