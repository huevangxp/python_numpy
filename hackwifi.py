import subprocess
import tkinter as tk
from tkinter import messagebox


def get_wifi_password(ssid: str) -> str | None:
    try:
        result = subprocess.run(
            [
                "security",
                "find-generic-password",
                "-D", "AirPort network password",
                "-a", ssid,
                "-gw"
            ],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return None
    except Exception as e:
        return str(e)


def show_password():
    ssid = ssid_entry.get().strip()
    if not ssid:
        messagebox.showwarning("Input Error", "Please enter a Wi-Fi SSID")
        return

    password = get_wifi_password(ssid)
    if password:
        messagebox.showinfo("Wi-Fi Password", f"SSID: {ssid}\nPassword: {password}")
    else:
        messagebox.showerror("Error", f"No password found for SSID: {ssid}")


# Create Tkinter window
root = tk.Tk()
root.title("Wi-Fi Password Finder")
root.geometry("400x200")

# Label + Input
tk.Label(root, text="Enter Wi-Fi SSID:", font=("Arial", 12)).pack(pady=10)
ssid_entry = tk.Entry(root, width=30, font=("Arial", 12))
ssid_entry.pack(pady=5)

# Button
tk.Button(root, text="Get Password", command=show_password, font=("Arial", 12)).pack(pady=20)

root.mainloop()
