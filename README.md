# nouserlogon-fix aka csgo popup handler

Main code contribution thanks to fantasy#0777, his method is way better than mine.

This script theorectically works on any resolution, as long as CSGO windows stays on top

The script features popup detector and screenshot saver, it will automatically log when there's a popup and save the screenshot of the window.

# Setting up Python and script

Download python from their website
https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe

You need to extract **_ALL_** files into the same folder, otherwise it will **_NOT_** work.


Open `cmd.exe` as admin and install these libraries using the command below
```
pip install pywin32
pip install keyboard
pip install pyautogui
pip install opencv-python
pip install Pillow
```
Locate your `pythonw.exe` in your python install path, open properties and set it to always run as administrator

# Running the script

Open the python script with IDLE, and Run the module

Profit!

You can run the command below in your csgo console to test if this works for you.
```
disconnect "anything you want to put in here"
```
