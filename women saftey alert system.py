import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class WomenSafetySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Women Safety Alert System")
        self.root.geometry("450x400")
        self.root.resizable(False, False)

        title = tk.Label(
            root,
            text="WOMEN SAFETY ALERT SYSTEM",
            font=("Arial", 18, "bold"),
            fg="darkred"
        )
        title.pack(pady=20)

        tk.Label(
            root,
            text="Emergency Contact Number:",
            font=("Arial", 12)
        ).pack(pady=5)

        self.contact_entry = tk.Entry(
            root,
            width=30,
            font=("Arial", 12)
        )
        self.contact_entry.pack(pady=5)

        self.status_label = tk.Label(
            root,
            text="Status: SAFE",
            font=("Arial", 14, "bold"),
            fg="green"
        )
        self.status_label.pack(pady=20)

        sos_button = tk.Button(
            root,
            text="🚨 SOS ALERT",
            font=("Arial", 18, "bold"),
            bg="red",
            fg="white",
            width=15,
            height=2,
            command=self.send_alert
        )
        sos_button.pack(pady=10)

        reset_button = tk.Button(
            root,
            text="Reset / I'm Safe",
            font=("Arial", 12),
            bg="green",
            fg="white",
            width=15,
            command=self.reset_status
        )
        reset_button.pack(pady=10)

        self.log = tk.Text(root, height=5, width=48)
        self.log.pack(pady=10)

    def send_alert(self):
        contact = self.contact_entry.get().strip()

        if not contact:
            messagebox.showwarning(
                "Missing Information",
                "Please enter an emergency contact number."
            )
            return

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        self.status_label.config(
            text="Status: SOS ALERT ACTIVATED",
            fg="red"
        )

        self.log.insert(
            tk.END,
            f"SOS Alert: {current_time}\n"
            f"Emergency Contact: {contact}\n"
            f"Status: Alert activated\n\n"
        )

        messagebox.showinfo(
            "SOS Alert",
            "Emergency alert activated!\n\n"
            f"Contact: {contact}\n"
            f"Time: {current_time}"
        )

    def reset_status(self):
        self.status_label.config(
            text="Status: SAFE",
            fg="green"
        )

        self.log.insert(
            tk.END,
            "Status changed to SAFE.\n\n"
        )


root = tk.Tk()
app = WomenSafetySystem(root)
root.mainloop()
