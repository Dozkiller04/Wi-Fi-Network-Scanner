# Wi-Fi Network Scanner 📶

A Python-based tool to scan nearby Wi-Fi networks and display essential information such as SSID, signal strength (dBm), and BSSID. Useful for analyzing signal strength and selecting the optimal Wi-Fi network for connectivity.

---

Features:
- Scans nearby Wi-Fi networks
- Displays SSID, BSSID, and signal strength (RSSI in dBm)
- Sorts networks by signal strength
- CLI and GUI versions available
- Cross-platform support (Windows/Linux)
- Lightweight and fast

---

Technologies Used:
- Python 3.x
- pywifi – Wi-Fi interface library
- tkinter – GUI interface (optional)
- subprocess – (used for Linux fallback support)

---

Folder Structure:

wifi-network-scanner/
├── main.py            # CLI runner
├── scanner.py         # Core scanning logic using pywifi
├── gui.py             # GUI interface with Tkinter (optional)
├── utils.py           # Utility functions (sorting, exporting)
├── requirements.txt   # Required Python packages
└── README.md          # Project documentation

---

Installation Instructions:

1. Clone the repository:
   git clone https://github.com/Dozkiller04/Wi-Fi-Network-Scanner.git
   cd Wi-Fi-Network-Scanner

2. Install required packages:
   pip install -r requirements.txt

Note: tkinter comes pre-installed with Python on most systems.

---

How to Use:

Run in CLI mode:
   python main.py

Run in GUI mode (optional):
   python gui.py

---

Example Output (CLI):

1. SSID: MyHomeWiFi
   Signal Strength: -40 dBm
   BSSID: A1:B2:C3:D4:E5:F6
------------------------------
2. SSID: GuestNetwork
   Signal Strength: -70 dBm
   BSSID: AA:BB:CC:DD:EE:FF
------------------------------

## 🎥 Project Demo (with Voice-over)

🎬 [Click here to watch the video demo](https://drive.google.com/file/d/1ugWrZr5Hl_Sy-oab5A3zvt5uaHNzHNUs/view?usp=drive_link)

---

Future Enhancements:
- Auto-refresh scanner every 10 seconds
- Connect to selected networks
- Export results to CSV
- Add signal strength chart using matplotlib
- Show security type (WPA2, WPA3, Open)

---

Author:
Soham Pramod Tayade
🎓 BSc Cyber & Digital Science
🏢 RISE Internship — Cybersecurity & Ethical Hacking
📍 Pune, Maharashtra
GitHub: https://github.com/Dozkiller04

---

License:
MIT License – feel free to use, modify, and share!
