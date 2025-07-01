# utils.py
import csv

def export_to_csv(networks, filename="wifi_results.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ssid', 'signal', 'bssid']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for net in networks:
            writer.writerow(net)

def sort_by_signal(networks):
    return sorted(networks, key=lambda x: x['signal'], reverse=True)

def display_networks(networks):
    for index, net in enumerate(networks):
        print(f"{index+1}. SSID: {net['ssid']}")
        print(f"   Signal: {net['signal']} dBm")
        print(f"   BSSID: {net['bssid']}")
        print("-" * 30)
