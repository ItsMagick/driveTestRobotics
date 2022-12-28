from . import usb_pixel_ring_v2
import usb.core
import usb.util


class LedControl:
    def __init__(self):
        self.dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.pixel_ring = usb_pixel_ring_v2.PixelRing(self.dev)

    def set_red(self):
        self.pixel_ring.set_color(None, 255, 0, 0)

    def set_green(self):
        self.pixel_ring.set_color(None, 0, 255, 0)

    def set_voice(self):
        self.pixel_ring.listen()
