# nouserlogon-fix aka csgo popup handler

Main code contribution thanks to **fantasy#0777**, his method is way better than mine.

Overall readability improvement, thanks to **selften#9285**.

This script theorectically works on any resolution, as long as CSGO windows stays on top

The script features popup detector and screenshot saver, it will automatically log when there's a popup and save the screenshot of the window.

# Setting up Python and script

Download python from their website
https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe

You need to extract **ALL** files into the same folder, otherwise it will **NOT** work. (except old version folder)

To make the script work, open CMD as administrator and copy the following command: `pip install -r https://raw.githubusercontent.com/fortXIV/nouserlogon-fix/main/required.txt`

Locate your `pythonw.exe` in your python installed folder, open properties and set it to always run as administrator

# Running the module

Right click the python file and Edit with IDLE, then Run the module.

Profit!

You can run the command below in your csgo console to test if this works for you.
```
disconnect "anything you want to put in here"
```
