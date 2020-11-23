import pyautogui
import time

delay = 10 # Inital Delay in Seconds
time.sleep(delay)

# name = r"C:\file.txt"   # File Name in Windows
name = r"/home/bob/Desktop/file.txt"   # File Name in Linux
interval = 0.07   # In Seconds

with open(name) as f:
	data = f.read()
	pyautogui.write(data, interval=interval)