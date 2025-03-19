import customtkinter as ctk
import speech
import session
import threading
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
close_btn = ctk.CTkButton(app, text="Close", command=lambda: session.cleanup(app))
close_btn.pack(pady=10)


# Function to greet the user (runs in a thread)
def greet():
  speech.speak("Hello! I am your PDA; currently in development stage.")

# Function to listen in the background
def listen_continuously():
  while True:
    command = speech.recognize_speech()
    if command:
      label.configure(text=f"You said: {command}")  # Update GUI text
      speech.speak(f"You said: {command}")

      if "exit" in command.lower():
        label.configure(text="Goodbye!")
        speech.speak("Okay I am closing now, meet you soon.")
        app.quit()
        break  # Stop loop

# Start greeting in a thread
threading.Thread(target=greet, daemon=True).start()

# Start listening in a separate thread
listening_thread = threading.Thread(target=listen_continuously, daemon=True)
listening_thread.start()

# Run the Tkinter loop
app.mainloop() # @type synchronous
speech.speak("Okay I am closing now, meet you soon.")