import pyqrcode
import png
from pyqrcode import QRCode

s = "https://play.hatchxr.com/@KamatchiKamaraj/Minecraft-replica--independent-project-"
url = pyqrcode.create(s)
url.svg("QR Code.svg", scale = 8)
url.png("QR Code.png", scale = 6) 