# AutoTyper - A Data Entry Tool 

Sometimes we have to write content in programs where copy-paste is not allowed, like in data entry software Notepad RT. There are many tools available online but almost all of them only provide trial versions. And requires big payment for continued access. And even if they are free, it is not wise to give complete access to a keyboard to any third-party software. So I wrote this simple-short python script which reads content from a text file then simulates keyboard typing. This Script works on both Linux and Windows.

## Releases
https://github.com/Parveshdhull/AutoTyper/releases

## Screenshot
<img src="Linux Executable/screenshot.png" alt="Screenshot" height="350"/>

## Python Version:
Python 3

## Prerequisite:
pip install pyautogui

### Additional Installation only for Linux
#### For Debian Based Systems
apt-get install python3-tk python3-dev
#### For Arch Linux Based Systems
pacman -S tk

## Parameters
* delay - Initial delay provided So that you get time for open file where you want to auto type content.

* name - Full path of input file.

* interval - Interval between each keystroke, This is provided so that software doesn't think you are bot.(0.07 is optimum for Notepad RT V.2)

## Usage

**Command Line**

	python autoTyper.py
	
**Graphical User Interface**

	python autoTyperGUI.py

## YouTube Tutorial
https://www.youtube.com/watch?v=NCKswqYyZmg

## Troubleshooting

For Notepad RTX++ check out this [Solution](https://github.com/Parveshdhull/AutoTyper/issues/2)

If you encounter any other problem and need my help, you can reach me at "right2trick@gmail.com"

## Liked my work?
<a href="https://www.buymeacoffee.com/parveshmonu" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Websites
https://github.com/Parveshdhull
<br />https://twitter.com/ParveshMonu
<br />https://youtube.com/right2trick






