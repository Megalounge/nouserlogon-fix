import pygetwindow as pgw
import pyautogui as pag
from datetime import datetime
import time

cnt = 0
i = 1

print("Script initialized, waiting")

def takess(x, y):
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Found error on {cnt} account(s), clicked OK')
        fname = "error" + str(i) + ".png"
        active_window = pgw.getActiveWindow()
        im1 = pag.screenshot(region=(active_window.left, active_window.top, active_window.width, active_window.height))
        im1.save(r"./errors/" + fname)
        
        btn_reconnect = pag.locateOnScreen('reconnect.png', region=(active_window.left, active_window.top, active_window.width, active_window.height), confidence=0.8)
        if btn_reconnect != None:
            reconnect_x, reconnect_y = pag.center(btn_reconnect)
            pag.leftClick(reconnect_x, reconnect_y)
            
                time.sleep(0.5)


while True:
    cs_instances = []

    for window in pgw.getAllWindows():
        # 389 309 = windowed
        # 389 280 = windowed borderless
        if (window.width == 389 or window.width == 383) and (window.height == 280 or window.height == 309):
            cs_instances.append(window)
    
    for window in cs_instances:
        x, y = window.center[0] + 40, window.center[1] + 8
        mid_x, mid_y = window.center

        btn_ok = pag.locateOnScreen('ok.png', region=(mid_x, mid_y, 160, 80), confidence=0.8)
        btn_confirm = pag.locateOnScreen('confirm.png', region=(mid_x, mid_y, 160, 80), confidence=0.8)
        btn_confirm_blue = pag.locateOnScreen('blue_confirm.png', region=(mid_x, mid_y, 160, 80), confidence=0.8)
        
        if btn_ok != None:
            btn_x, btn_y = pag.center(btn_ok)
            pag.leftClick(btn_x, btn_y)
            cnt += 1
            takess(x, y)
            i += 1
            time.sleep(0.05)
        elif btn_confirm != None:
            btn_x, btn_y = pag.center(btn_confirm)
            pag.leftClick(btn_x, btn_y)
            cnt += 1
            takess(x, y)
            i += 1
            time.sleep(0.05)
        elif btn_confirm_blue != None:
            btn_x, btn_y = pag.center(btn_confirm_blue)
            pag.leftClick(btn_x, btn_y)
            cnt += 1
            takess(x, y)
            i += 1
            time.sleep(0.05)

    time.sleep(0.5)
