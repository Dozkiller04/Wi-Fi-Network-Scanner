# main.py

from scanner import scan_networks
from utils import sort_by_signal, display_networks

def main():
    print("Scanning Wi-Fi networks...\n")
    networks = scan_networks()
    sorted_networks = sort_by_signal(networks)
    display_networks(sorted_networks)

if __name__ == "__main__":
    main()
