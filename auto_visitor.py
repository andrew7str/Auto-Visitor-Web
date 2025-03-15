import requests
import random
import time
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class AutoVisitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Visitor Website By Mr.exe")
        self.root.geometry("400x400")

        # Label dan Input URL
        tk.Label(root, text="Website URL:").pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        # Label dan Input Jumlah Kunjungan
        tk.Label(root, text="Jumlah Kunjungan:").pack()
        self.visits_entry = tk.Entry(root, width=10)
        self.visits_entry.pack()

        # Tombol Start dan Stop
        self.start_btn = tk.Button(root, text="Start", command=self.start_visiting)
        self.start_btn.pack(pady=5)

        self.stop_btn = tk.Button(root, text="Stop", command=self.stop_visiting, state=tk.DISABLED)
        self.stop_btn.pack()

        # Log Box
        self.log_box = scrolledtext.ScrolledText(root, width=50, height=10)
        self.log_box.pack(pady=5)

        self.running = False

    def visit_website(self):
        url = self.url_entry.get()
        try:
            visits = int(self.visits_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Jumlah kunjungan harus berupa angka!")
            return
        
        self.log_box.insert(tk.END, f"Memulai kunjungan ke {url}...\n")
        self.log_box.yview(tk.END)

        self.running = True
        for i in range(visits):
            if not self.running:
                self.log_box.insert(tk.END, "Proses dihentikan.\n")
                self.log_box.yview(tk.END)
                return

            try:
                response = requests.get(url)
                status = f"({i+1}) {url} - {response.status_code}\n"
                self.log_box.insert(tk.END, status)
            except Exception as e:
                self.log_box.insert(tk.END, f"({i+1}) Error: {e}\n")
            
            self.log_box.yview(tk.END)
            delay = random.randint(1, 5)
            time.sleep(delay)

        self.log_box.insert(tk.END, "Kunjungan selesai!\n")
        self.log_box.yview(tk.END)
        self.stop_btn.config(state=tk.DISABLED)
        self.start_btn.config(state=tk.NORMAL)

    def start_visiting(self):
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        threading.Thread(target=self.visit_website, daemon=True).start()

    def stop_visiting(self):
        self.running = False
        self.stop_btn.config(state=tk.DISABLED)
        self.start_btn.config(state=tk.NORMAL)

# Jalankan aplikasi
root = tk.Tk()
app = AutoVisitorApp(root)
root.mainloop()
