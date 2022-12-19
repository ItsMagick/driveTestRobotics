#!/usr/bin/python3.8

import tuning
import usb.core
import usb.util
import time

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

if dev:
    Mic_tuning = tuning.Tuning(dev)
    
    while True:
        try:
            if Mic_tuning.is_voice():
                print(Mic_tuning.direction)
            
            # time.sleep(1)
        except KeyboardInterrupt:
            break
