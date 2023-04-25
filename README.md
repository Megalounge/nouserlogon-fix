# nouserlogon-fix aka csgo popup handler

This script theorectically works on any resolution, you just have to change the ROWS and COLUMNS according to your usual csgo windows setup, for example in 1080p there are 2 ROWS and 5 COLUMNS

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
Locate your pythonw.exe in your python install path, open properties and set it to always run as administrator

# Running the script

Open the python script with IDLE, and Run the module

Profit!

You can run the command `disconnect "No user logon."` in your csgo console to test if this works for you.
