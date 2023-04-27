import pygetwindow as pgw
import pyautogui as pag
from datetime import datetime
import time

cnt = 1
i = 1

print("Script initialized, waiting")

def takess(x, y):
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Found error on {cnt} account(s), clicked OK.')
        fname = "error" + str(i) + ".png"
        active_window = pgw.getActiveWindow()
        im1 = pag.screenshot(region=(active_window.left, active_window.top, active_window.width, active_window.height))
        im1.save(r"./errors/" + fname)
        
def is_reconnect(x, y):
        active_window = pgw.getActiveWindow()
        btn_reconnect = pag.locateOnScreen('reconnect.png', region=(active_window.left, active_window.top, active_window.width, active_window.height), confidence=0.9)
        if btn_reconnect != None:
            print(f'[{datetime.now().strftime("%H:%M:%S")}] Found RECONNECT button, reconnecting...')
            reconnect_x, reconnect_y = pag.center(btn_reconnect)
            time.sleep(2)
            pag.leftClick(reconnect_x, reconnect_y)
            
            time.sleep(0.5)


while True:
    time.sleep(0.1)
    cs_instances = []

    for window in pgw.getAllWindows():
        # 389 309 = windowed
        # 389 280 = windowed borderless
        try:
           if (window.width == 389 or window.width == 383) and (window.height == 280 or window.height == 309):
                cs_instances.append(window)
        except pgw.PyGetWindowException:
                print(f'[{datetime.now().strftime("%H:%M:%S")}] Caught error! Please check your CSGO status.')
                continue
    
    for window in cs_instances:
        x, y = window.center[0] + 40, window.center[1] + 8
        mid_x, mid_y = window.center

        btn_ok = pag.locateOnScreen('ok.png', region=(mid_x, mid_y, 100, 100), confidence=0.8)
        if btn_ok != None:
            takess(x, y)
            btn_x, btn_y = pag.center(btn_ok)
            pag.leftClick(btn_x, btn_y)
            time.sleep(0.2)
            pag.leftClick(btn_x, btn_y)
            cnt += 1
            time.sleep(1)
            is_reconnect(x, y)
            i += 1
            time.sleep(2)
        else:
            btn_confirm = pag.locateOnScreen('confirm.png', region=(mid_x, mid_y, 100, 100), confidence=0.8)
            if btn_confirm != None:
                takess(x, y)
                btn_x, btn_y = pag.center(btn_confirm)
                pag.leftClick(btn_x, btn_y)
                time.sleep(0.2)
                pag.leftClick(btn_x, btn_y)
                cnt += 1
                time.sleep(1)
                is_reconnect(x, y)
                i += 1
                time.sleep(2)
            else:
                btn_confirm_blue = pag.locateOnScreen('blue_confirm.png', region=(mid_x, mid_y, 100, 100), confidence=0.8)
                if btn_confirm_blue != None:
                    takess(x, y)
                    btn_x, btn_y = pag.center(btn_confirm_blue)
                    pag.leftClick(btn_x, btn_y)
                    time.sleep(0.2)
                    pag.leftClick(btn_x, btn_y)
                    cnt += 1
                    time.sleep(1)
                    is_reconnect(x, y)
                    i += 1
                    time.sleep(2)
                else:
                    continue

    time.sleep(2)

