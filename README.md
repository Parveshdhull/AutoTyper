# AutoTyper - A Data Entry Tool 

Sometimes we have to write content in programs where copy-paste is not allowed, like in data entry software Notepad RT. There are many tools available online but almost all of them only provide trial versions. And requires big payment for continued access. And even if they are free, it is not wise to give complete access to a keyboard to any third-party software. So I wrote this simple-short python script which reads content from a text file then simulates keyboard typing. This Script works on both Linux and Windows.

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
	python autoTyper.py

## Troubleshooting
If you encounter any problem and need my help,you can reach me at "git.hrca@gmail.com"






