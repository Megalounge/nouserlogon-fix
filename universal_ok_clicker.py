import pygetwindow as pgw
import pyautogui as pag
from datetime import datetime
import time
import win32process as w32p

ErrorsCount = 1

print("Script initialized, waiting")

def ErrorFound(x, y):
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Found error on {ErrorsCount} account(s), clicked OK.')
        FileName = "error" + str(ErrorsCount) + ".png"
        ActiveWindow = pgw.getActiveWindow()
        ErrorImage = pag.screenshot(region=(ActiveWindow.left, ActiveWindow.top, ActiveWindow.width, ActiveWindow.height))
        ErrorImage.save(r"./errors/" + FileName)
        
def ReconnectFound(x, y):
        ActiveWindow = pgw.getActiveWindow()
        ReconnectButton = pag.locateOnScreen('./img/reconnect.png', region=(ActiveWindow.left, ActiveWindow.top, ActiveWindow.width, ActiveWindow.height), confidence=0.9)
        if ReconnectButton != None:
            print(f'[{datetime.now().strftime("%H:%M:%S")}] Found RECONNECT button, reconnecting...')
            ReconnectButton_x, ReconnectButton_y = pag.center(ReconnectButton)
            time.sleep(2)
            pag.leftClick(ReconnectButton_x, ReconnectButton_y)
            
            time.sleep(0.5)

while True:
    time.sleep(0.1)
    CSWindows = []

    for Window in pgw.getAllWindows():
        try:
           if Window.width == 389 and Window.height == 309:
                CSWindows.append(Window)
        except pgw.PyGetWindowException:
                print(f'[{datetime.now().strftime("%H:%M:%S")}] Caught error! Please check your CSGO status.')
                CSWindows = [w for w in CSWindows if w32p.GetWindowThreadProcessId(w)[1] != Window.pid]
    
    for Window in CSWindows:
        try:
            x, y = Window.center[0] + 40, Window.center[1] + 8
        except pgw.PyGetWindowException:
            print(f'[{datetime.now().strftime("%H:%M:%S")}] Caught error! Please check your CSGO status.')
            CSWindows = [w for w in CSWindows if w32p.GetWindowThreadProcessId(w)[1] != Window.pid]
        
        Window_x, Window_y = Window.center

        OKButton = pag.locateOnScreen('./img/ok.png', region=(Window_x, Window_y, 100, 100), confidence=0.8)
        ConfirmButton = pag.locateOnScreen('./img/confirm.png', region=(Window_x, Window_y, 100, 100), confidence=0.8)
        BlueConfirmButton = pag.locateOnScreen('./img/blue_confirm.png', region=(Window_x, Window_y, 100, 100), confidence=0.8)

        if OKButton != None:
            ErrorFound(x, y)
            Button_x, Button_y = pag.center(OKButton)
            pag.leftClick(Button_x, Button_y)
            time.sleep(0.2)
            pag.leftClick(Button_x, Button_y)
            ErrorsCount += 1
            time.sleep(1)
            ReconnectFound(x, y)
            time.sleep(2)
        elif ConfirmButton != None:
            ErrorFound(x, y)
            Button_x, Button_y = pag.center(ConfirmButton)
            pag.leftClick(Button_x, Button_y)
            time.sleep(0.2)
            pag.leftClick(Button_x, Button_y)
            ErrorsCount += 1
            time.sleep(1)
            ReconnectFound(x, y)
            time.sleep(2)
        elif BlueConfirmButton != None:
            ErrorFound(x, y)
            Button_x, Button_y = pag.center(BlueConfirmButton)
            pag.leftClick(Button_x, Button_y)
            time.sleep(0.2)
            pag.leftClick(Button_x, Button_y)
            ErrorsCount += 1
            time.sleep(1)
            ReconnectFound(x, y)
            time.sleep(2)
