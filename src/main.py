import customtkinter as ctk
# import tkinter as tk

# Initialize Tkinter
root = ctk.CTk()
root.title("Neura - PDA")
# root.overrideredirect(True)  # Removes the title bar
root.attributes("-topmost", True)  # Keeps window above other windows


# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Window size
window_width = 300
window_height = 150

# Calculate position (Bottom Right)
x_position = screen_width - window_width - 10  # 10px margin from right
y_position = screen_height - window_height - 50  # 50px margin from bottom

# Set geometry
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(False, False)

# Add a label
label = ctk.CTkLabel(root, text="Hello! I am your PDA.", font=("Arial", 16))
label.pack(pady=20)

# Add a close button
close_btn = ctk.CTkButton(root, text="Close", command=root.destroy)
close_btn.pack(pady=10)

# Run the Tkinter loop
root.mainloop()
