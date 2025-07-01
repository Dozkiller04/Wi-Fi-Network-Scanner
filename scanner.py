# scanner.py

import pywifi
import time

def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(3)  # Wait for scan to complete
    results = iface.scan_results()

    networks = []
    for network in results:
        networks.append({
            'ssid': network.ssid,
            'signal': network.signal,
            'bssid': network.bssid,
            'auth': network.auth,
            'akm': network.akm
        })
    return networks
