import tkinter as tk
import pyautogui
from PIL import ImageGrab
import keyboard

def get_color_at_cursor():
    x, y = pyautogui.position()
    screen = ImageGrab.grab()
    color = screen.getpixel((x, y))
    return x, y, color

def update_gui():
    x, y, color = get_color_at_cursor()

    color_hex = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}".upper()
    canvas.itemconfig(color_rect, fill=color_hex)
    color_label.config(text=f"RGB: {color}\nHEX: {color_hex}")

    window.geometry(f"250x70+{x+20}+{y+20}")
    window.after(50, update_gui)

def create_rounded_rectangle(x1, y1, x2, y2, radius=10, **kwargs):
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

def launch_app():
    global window, canvas, color_rect, color_label

    window = tk.Tk()
    window.overrideredirect(True)
    window.attributes("-topmost", True)
    window.config(bg="black")

    canvas = tk.Canvas(window, width=60, height=50, bg="black", highlightthickness=0)
    canvas.place(x=10, y=15)

    color_rect = create_rounded_rectangle(0, 0, 50, 50, radius=15, fill="black", outline="")

    color_label = tk.Label(window, text="", font=("Helvetica", 12), fg="white", bg="black", anchor="w")
    color_label.place(x=70, y=25)
    update_gui()

    window.mainloop()
    

def close_app():
    window.destroy()
    keyboard.unhook_all()
    

keyboard.add_hotkey("win+`", launch_app)
keyboard.wait()
