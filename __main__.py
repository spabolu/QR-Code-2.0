import time
import math
import qrcode
import os
import shutil
import base64
from PIL import Image     
import qrcode 

filename = "test.jpg"
readablefile = open(filename, "rb")
encoded = base64.b64encode(readablefile.read())
qrCode = qrcode.make(encoded)

print(encoded)
input()
