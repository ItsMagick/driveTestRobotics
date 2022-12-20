
from usb_pixel_ring_v2 import PixelRing
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
print(dev)
if dev:
    pixel_ring = PixelRing(dev)
    pixel_ring.set_color(None, 200, 0,0)
