# 📶 Wi-Fi Network Scanner

A Python-based tool to scan nearby Wi-Fi networks and display essential information such as SSID, signal strength (dBm), and BSSID. Useful for analyzing signal strength and selecting the optimal Wi-Fi network for connectivity.

---

## ✨ Features

- Scans nearby Wi-Fi networks
- Displays SSID, BSSID, and signal strength (RSSI in dBm)
- Sorts networks by signal strength
- CLI and GUI versions available
- Cross-platform support (Windows/Linux)
- Lightweight and fast

---

## 🛠️ Technologies Used

- Python 3.x
- `pywifi` – Wi-Fi interface library
- `tkinter` – GUI interface (optional)
- `subprocess` – Linux fallback support

---

## 📁 Folder Structure

wifi-network-scanner/
├── main.py # CLI runner
├── scanner.py # Core scanning logic using pywifi
├── gui.py # GUI interface with Tkinter
├── utils.py # Utility functions
├── requirements.txt # Required Python packages
├── screenshots/ # Output screenshots
│ ├── Output_01.png # CLI output
│ └── GUI_Output_02.png # GUI output
└── README.md # Project documentation

yaml
Copy code

---

## 📦 Installation Instructions

```bash
git clone https://github.com/Dozkiller04/Wi-Fi-Network-Scanner.git
cd Wi-Fi-Network-Scanner
pip install -r requirements.txt
💡 tkinter is usually pre-installed with Python. If not, install it manually.

⚙️ How to Use
▶️ Run in CLI mode:
bash
Copy code
python main.py
🖥️ Run in GUI mode:
bash
Copy code
python gui.py
## 📸 Project Screenshots

### 🔹 CLI Interface Output  
![CLI Output](screenshots/Output_01.png)

### 🔹 GUI Interface Output  
![GUI Output](screenshots/GUI_Output_02.png)

---

## 🎬 Project Demo (with Voice-over)

📽️ Watch the full video demo here:  
👉 [Click to Watch Video Demo](https://drive.google.com/file/d/1ugWrZr5Hl_Sy-oab5A3zvt5uaHNzHNUs/view?usp=drive_link)


🚀 Future Enhancements
Auto-refresh scanner every 10 seconds
Connect to selected networks
Export results to CSV
Add signal strength chart using matplotlib
Show Wi-Fi security type (WPA2/WPA3/Open)

👨‍💻 Author
Soham Pramod Tayade
🎓 BSc Cyber & Digital Science
🏢 RISE Internship – Cybersecurity & Ethical Hacking
📍 Pune, Maharashtra
🔗 GitHub: Dozkiller04
