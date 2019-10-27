import network
import time


def connect():
    ssid = "YOUR SSID"
    password = "YOUR PASSWORD"
    wait = 60  # seconds

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print(".", end="")
            time.sleep(1)
            if wait > 0:
                wait -= 1
            else:
                print("failed to connect to network")
                return
    print("network config:", wlan.ifconfig())
