import customtkinter as ctk
import os
# import tkinter as tk

# Initialize Tkinter
app = ctk.CTk()
app.title("Neura - PDA")
# icon_path = os.path.abspath("assets/neura_logo.ico")
# app.iconbitmap(icon_path)
# app.overrideredirect(True)  # Removes the title bar
app.attributes("-topmost", True)  # Keeps window above other windows

# Get screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Window size
window_width = 300
window_height = 150

# Calculate position (Bottom Right)
x_position = screen_width - window_width - 10  # 10px margin from right
y_position = screen_height - window_height - 50  # 50px margin from bottom

# Set geometry
app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
app.resizable(False, False)

# Add a label
label = ctk.CTkLabel(app, text="Hello! I am your PDA.", font=("Arial", 16))
label.pack(pady=20)

# Add a close button
close_btn = ctk.CTkButton(app, text="Close", command=app.destroy)
close_btn.pack(pady=10)

# Run the Tkinter loop
app.mainloop()
