import tkinter as tk
import random
import time
import threading
# Optional voice
try:
    import pyttsx3
    engine = pyttsx3.init()
    def speak(text):
        engine.say(text)
        engine.runAndWait()
except:
    def speak(text):
        pass

# Create window
root = tk.Tk()
root.title("Smart Wheelchair System")
root.geometry("500x500")
root.config(bg="#0f172a")

# Title
title = tk.Label(root, text="SMART WHEELCHAIR", font=("Arial", 18, "bold"), fg="white", bg="#0f172a")
title.pack(pady=10)

# Status label
status = tk.Label(root, text="System Ready", font=("Arial", 14), fg="cyan", bg="#0f172a")
status.pack(pady=10)

# Distance label
distance_label = tk.Label(root, text="Distance: -- cm", font=("Arial", 12), fg="white", bg="#0f172a")
distance_label.pack(pady=5)

# Functions
def move_forward():
    status.config(text="➡ Moving Forward", fg="green")
    speak("Moving forward. Please stay alert")

def move_backward():
    status.config(text="⬅ Moving Backward", fg="green")
    speak("Moving backward. Be careful")

def stop():
    status.config(text="⛔ Stopped", fg="yellow")
    speak("Wheelchair stopped")

def emergency():
    status.config(text="🚨 Emergency Alert Sent!", fg="orange")
    root.update()  # force UI update
    speak("Emergency alert has been sent")

def update_distance():
    distance = random.randint(5, 100)
    distance_label.config(text=f"Distance: {distance} cm")

    if distance < 20:
        status.config(text="⚠ Obstacle Detected!", fg="red")
        speak("Warning. Obstacle detected. Stopping wheelchair")
    else:
        root.after(2000, update_distance)
def move_left():
    status.config(text="⬅ Turning Left", fg="green")
    speak("Turning left")

def move_right():
    status.config(text="➡ Turning Right", fg="green")
    speak("Turning right")
speak("Smart wheelchair system activated")
# Buttons
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=20)

btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=20)

# Forward
tk.Button(btn_frame, text="Forward", width=12,
          command=move_forward, bg="green", fg="white").grid(row=0, column=1, pady=5)

# Left - Stop - Right
tk.Button(btn_frame, text="Left", width=12,
          command=move_left, bg="purple", fg="white").grid(row=1, column=0, padx=5)

tk.Button(btn_frame, text="Stop", width=12,
          command=stop, bg="red", fg="white").grid(row=1, column=1, pady=5)

tk.Button(btn_frame, text="Right", width=12,
          command=move_right, bg="black", fg="white").grid(row=1, column=2, padx=5)

# Backward
tk.Button(btn_frame, text="Backward", width=12,
          command=move_backward, bg="blue", fg="white").grid(row=2, column=1, pady=5)

# Emergency button (separate)
tk.Button(root, text="Emergency", width=15,
          command=emergency, bg="orange", fg="white").pack(pady=10)
# Start sensor simulation
update_distance()

# Run app
root.mainloop()
