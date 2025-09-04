import tkinter as tk

def show_table():
    try:
        n = int(number.get())
        # Clear old results
        for widget in result_frame.winfo_children():
            widget.destroy()

        # Show multiplication table
        for i in range(1, 11):
            label = tk.Label(result_frame, text=f"{i} x {n} = {i * n}", font=("Arial", 12))
            label.pack()
    except ValueError:
        # Handle if user enters non-numeric
        label = tk.Label(result_frame, text="Please enter a valid number!", fg="red")
        label.pack()

root = tk.Tk()
root.title("Bansu")
root.geometry("400x400")

# Input box
number = tk.Entry(root, width=10, font=("Arial", 14))
number.pack(pady=10)

# Submit button
button = tk.Button(root, text="Submit", command=show_table, font=("Arial", 12))
button.pack(pady=5)

# Frame to hold results
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

root.mainloop()
