import tkinter as tk
import time

def countdown(time_remaining):
    if time_remaining > 0:
        mins, secs = divmod(time_remaining, 60)
        time_str = "{:02d}:{:02d}".format(mins, secs)
        label.config(text=time_str)
        root.after(1000, countdown, time_remaining - 1)
    else:
        label.config(text="时间到！")

def start_timer():
    countdown(25 * 60)

root = tk.Tk()
root.title("专注时钟")

label = tk.Label(root, font=("Courier", 30), bg="lightblue", width=10)
label.pack(pady=10)

start_button = tk.Button(root, text="开始", command=start_timer)
start_button.pack()

root.mainloop()
