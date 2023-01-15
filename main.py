#!/usr/bin/env python3
"""PyBluez ble example beacon.py
Advertises a bluethooth low energy beacon for 15 seconds.
"""

import time

from bluetooth.ble import BeaconService

UUID = "CFFD85BB-67E0-9CD4-B2D0-BE5A7ECAC915"
service = BeaconService()

# service.start_advertising("11111111-2222-3333-4444-555555555555",
try:
    for x in range(1, 300):
        print("hello: {}".format(x))
        service.start_advertising(UUID, (x * 256) % 65535, 1 * 256, -39, 200)
        time.sleep(1)
finally:
    service.stop_advertising()
    print("Done.")
