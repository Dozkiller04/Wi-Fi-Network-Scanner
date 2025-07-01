# gui.py

import tkinter as tk
from tkinter import ttk
from scanner import scan_networks
from utils import sort_by_signal

def display_results():
    networks = sort_by_signal(scan_networks())
    tree.delete(*tree.get_children())
    for net in networks:
        tree.insert("", "end", values=(net['ssid'], net['signal'], net['bssid']))

app = tk.Tk()
app.title("Wi-Fi Network Scanner")
app.geometry("600x400")

tree = ttk.Treeview(app, columns=("SSID", "Signal", "BSSID"), show="headings")
tree.heading("SSID", text="SSID")
tree.heading("Signal", text="Signal Strength (dBm)")
tree.heading("BSSID", text="BSSID")
tree.pack(fill=tk.BOTH, expand=True)

btn = tk.Button(app, text="Scan", command=display_results)
btn.pack(pady=10)

app.mainloop()
