from MyQR import myqr
import cv2 as cv
from pyzbar import pyzbar
# myqr.run(words="ZengJie")

img=cv.imread("qrcode.png")
data=pyzbar.decode(img)
print(data[0].data.decode('utf-8'))


