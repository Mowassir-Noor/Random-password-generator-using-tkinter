import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    character_sets = {
        "uppercase": string.ascii_uppercase if use_uppercase.get() else "",
        "lowercase": string.ascii_lowercase if use_lowercase.get() else "",
        "numbers": string.digits if use_numbers.get() else "",
        "special_chars": string.punctuation if use_special_chars.get() else ""
    }
    
    selected_chars = "".join(character_sets.values())
    password_length = password_length_slider.get()
    
    if not selected_chars:
        messagebox.showerror("Error", "Please select at least one character set.")
        return
    
    if password_length <= 0:
        messagebox.showerror("Error", "Password length should be greater than 0.")
        return
    
    password = ''.join(random.choice(selected_chars) for _ in range(password_length))
    password_display.config(text=f"Generated Password: {password}")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Initialize Tkinter variables
use_uppercase = tk.BooleanVar()
use_lowercase = tk.BooleanVar()
use_numbers = tk.BooleanVar()
use_special_chars = tk.BooleanVar()
password_length_slider = tk.IntVar()

# Create a frame to organize widgets
frame = tk.LabelFrame(window, text="Password Options", padx=20, pady=20)
frame.pack(padx=20, pady=20)

# Character set checkboxes
tk.Checkbutton(frame, text="Uppercase Letters", variable=use_uppercase).pack(anchor="w")
tk.Checkbutton(frame, text="Lowercase Letters", variable=use_lowercase).pack(anchor="w")
tk.Checkbutton(frame, text="Numbers", variable=use_numbers).pack(anchor="w")
tk.Checkbutton(frame, text="Special Characters", variable=use_special_chars).pack(anchor="w")

# Password length slider
tk.Label(frame, text="Password Length").pack(anchor="w")
tk.Scale(frame, from_=1, to=20, variable=password_length_slider, orient="horizontal").pack()

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Password display label
password_display = tk.Label(window, text="", font=("Helvetica", 14))
password_display.pack(pady=10)

# Start the main loop
window.mainloop()
