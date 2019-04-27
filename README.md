# BARbQR

A Barcode and QR code reader using python, opencv and zbar.

## Requirements
1. Python 3.x
2. OpenCV
3. zbar

## How to run?
In terminal, type  `python3 scanner.py`

`image = cv2.imread(test_image.png)` - to read image

`barcodes = pyzbar.decode(image)` - zbar detect and decode the barcodes in image.
