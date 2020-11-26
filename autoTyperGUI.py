#!/bin/python3

import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
import webbrowser
import time
import multiprocessing
import sys


def typing():
	interval = float(ent_interval.get())
	delay = int(ent_delay.get())
	time.sleep(delay)
	data = txt_box.get("1.0", tk.END)
	import pyautogui
	pyautogui.write(data, interval=interval)


def start_typing():
	global t1
	t1 =  multiprocessing.Process(target=typing)
	t1.start()
	messagebox.showinfo("Message", "Click on the Window where you want text to be typed.") 


def stop_typing():
	t1.terminate() 
	t1.join()
	sys.stdout.flush()
	global i


def exit_program():
	sys.exit()

def select_all(event):
    txt_box.tag_add(tk.SEL, "1.0", tk.END)
    txt_box.mark_set(tk.INSERT, "1.0")
    txt_box.see(tk.INSERT)
    return 'break'


def callback(url):
    webbrowser.open_new(url)


def create_about_window():
	about_window = tk.Toplevel(window)
	about_window.title("About")

	lbl_name = tk.Label(text="Version - Auto Typer 1.0", master=about_window, font='Helvetica 15')
	lbl_name.grid(row=0, column=0, pady=(15,5), padx=10)

	lbl_developer = tk.Label(text="Developer - Parvesh Monu", master=about_window, font='Helvetica 10')
	lbl_developer.grid(row=1, column=0,  pady=5, padx=10)

	lbl_twitter = tk.Label(text="Follow - https://twitter.com/parveshmonu", master=about_window, font='Helvetica 10', fg="blue", cursor="hand2")
	lbl_twitter.grid(row=2, column=0, pady=5, padx=10)
	lbl_twitter.bind("<Button-1>", lambda e: callback("https://twitter.com/parveshmonu"))

	lbl_github = tk.Label(text="Github - https://github.com/Parveshdhull", master=about_window, font='Helvetica 10', fg="blue", cursor="hand2")
	lbl_github.grid(row=3, column=0, pady=5, padx=10,)
	lbl_github.bind("<Button-1>", lambda e: callback("https://github.com/Parveshdhull"))

	lbl_youtube= tk.Label(text="YouTube - https://youtube.com/right2trick", master=about_window, font='Helvetica 10', fg="blue", cursor="hand2")
	lbl_youtube.grid(row=4, column=0, pady=10, padx=10,)
	lbl_youtube.bind("<Button-1>", lambda e: callback("https://youtube.com/right2trick"))

	buy_coffee = tk.Button(text="Buy me a coffee", master=about_window)
	buy_coffee.grid(row=5,column=0, padx=10, pady=(10,20))
	buy_coffee.bind("<Button-1>", lambda e: callback("https://www.buymeacoffee.com/parveshmonu"))

	about_window.mainloop()


def create_main_window():
	window.title("Auto Typer")

	# Params Frame
	frm_params = tk.Frame()
	frm_params.grid(row=0,column=0)

	# Delay
	lbl_delay = tk.Label(text="Inital Delay (In Sec)", master=frm_params)
	lbl_delay.grid(row=0,column=0, padx=50, pady=5)

	global ent_delay
	ent_delay =  tk.Entry(justify='center', master=frm_params)
	ent_delay.insert(0, "5")
	ent_delay.grid(row=1,column=0, padx=50)

	# Interval
	lbl_interval = tk.Label(text="Interval (In Sec)", master=frm_params)
	lbl_interval.grid(row=0,column=1, padx=50, pady=5)

	global ent_interval
	ent_interval =  tk.Entry(justify='center', master=frm_params)
	ent_interval.insert(0, "0.07")
	ent_interval.grid(row=1,column=1, padx=50)

	# Data
	lbl_data = tk.Label(text="Paste Text Here", font='Helvetica 18 bold' )
	lbl_data.grid(row=3,column=0, pady=(10,2))

	global txt_box
	txt_box = scrolledtext.ScrolledText(window, undo=True)
	txt_box.grid(row=4,column=0)

	txt_box.bind("<Control-Key-a>", select_all)
	txt_box.bind("<Control-Key-A>", select_all)

	# Buttons Frame
	frm_buttons = tk.Frame()
	frm_buttons.grid(row=5,column=0)

	# Start
	start = tk.Button(text="Start", master=frm_buttons, command=start_typing)
	start.grid(row=0,column=0, padx=10, pady=10)

	# Stop
	start = tk.Button(text="Stop", master=frm_buttons, command=stop_typing)
	start.grid(row=0,column=1, padx=10, pady=10)

	# Exit
	start = tk.Button(text="Exit", master=frm_buttons, command=exit_program)
	start.grid(row=0,column=2, padx=10, pady=10)

	# About
	start = tk.Button(text="About", command=create_about_window)
	start.grid(row=6,column=0, padx=10, pady=10)

	window.mainloop()


window = tk.Tk()
create_main_window()


# # Gravity
# window.columnconfigure(0, weight=1)
# window.rowconfigure(3, weight=1)
# window.columnconfigure(1, weight=1)
# window.rowconfigure(1, weight=1)