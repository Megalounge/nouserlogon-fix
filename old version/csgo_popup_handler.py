from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Width and height of each window
WINDOW_WIDTH = 385
WINDOW_HEIGHT = 307

# Number of windows in each row and column
ROWS = 2
COLUMNS = 5

# Coordinates of the top-left corner of each window
WINDOW_COORDS = [(x * WINDOW_WIDTH, y * WINDOW_HEIGHT) for y in range(ROWS) for x in range(COLUMNS)]

# Offset of the OK button within the popup window
OK_BUTTON_OFFSET_NOUSERLOGON = (115, 42)
OK_BUTTON_OFFSET_STEAMREQUIRED = (150, 42)
OK_BUTTON_OFFSET_REMOTEHOST = (135, 42)


time.sleep(10)
def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_ok(x, y):
    # Click OK button
    click(ok_x, ok_y)
    time.sleep(2.0)


def click_ok_and_reconnect(x, y):
    # Click OK button
    click(ok_x, ok_y)
    time.sleep(2.0)

    # Click Reconnect
    win_x, win_y = WINDOW_COORDS[window_idx][0] + window_x - (window_idx % COLUMNS) * WINDOW_WIDTH + 170, \
                   WINDOW_COORDS[window_idx][1] + window_y - (window_idx // COLUMNS) * WINDOW_HEIGHT - 100
    click(win_x, win_y)

iteration = 1

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    location_nouserlogon = pyautogui.locateOnScreen('no_user_logon.png', grayscale=True, confidence=0.8)
    location_steamrequired = pyautogui.locateOnScreen('steam_required.png', grayscale=True, confidence=0.8)
    location_remotehost = pyautogui.locateOnScreen('remote_host.png', grayscale=True, confidence=0.8)
    
    if location_nouserlogon:
        print(f"count: {iteration}{' ' * 5}time: {current_time}")
        print(f"No user logon detected, clicking OK and reconnect.")
        iteration += 1
        window_x, window_y = location_nouserlogon.left, location_nouserlogon.top
        window_idx = (window_x // WINDOW_WIDTH) + (window_y // WINDOW_HEIGHT) * COLUMNS
        ok_x, ok_y = WINDOW_COORDS[window_idx][0] + window_x - (window_idx % COLUMNS) * WINDOW_WIDTH + OK_BUTTON_OFFSET_NOUSERLOGON[0], \
            WINDOW_COORDS[window_idx][1] + window_y - (window_idx // COLUMNS) * WINDOW_HEIGHT + OK_BUTTON_OFFSET_NOUSERLOGON[1]
        click_ok_and_reconnect(ok_x, ok_y)
        time.sleep(2.0)
    elif location_steamrequired:
        print(f"count: {iteration}{' ' * 5}time: {current_time}")
        print(f"Steam required detected, clicking OK.")
        iteration += 1
        window_x, window_y = location_steamrequired.left, location_steamrequired.top
        window_idx = (window_x // WINDOW_WIDTH) + (window_y // WINDOW_HEIGHT) * COLUMNS
        ok_x, ok_y = WINDOW_COORDS[window_idx][0] + window_x - (window_idx % COLUMNS) * WINDOW_WIDTH + OK_BUTTON_OFFSET_STEAMREQUIRED[0], \
            WINDOW_COORDS[window_idx][1] + window_y - (window_idx // COLUMNS) * WINDOW_HEIGHT + OK_BUTTON_OFFSET_STEAMREQUIRED[1]
        click_ok(ok_x, ok_y)
        time.sleep(2.0)
    elif location_remotehost:
        print(f"count: {iteration}{' ' * 5}time: {current_time}")
        print(f"Remote host detected, clicking OK and reconnect.")
        iteration += 1
        window_x, window_y = location_remotehost.left, location_remotehost.top
        window_idx = (window_x // WINDOW_WIDTH) + (window_y // WINDOW_HEIGHT) * COLUMNS
        ok_x, ok_y = WINDOW_COORDS[window_idx][0] + window_x - (window_idx % COLUMNS) * WINDOW_WIDTH + OK_BUTTON_OFFSET_REMOTEHOST[0], \
            WINDOW_COORDS[window_idx][1] + window_y - (window_idx // COLUMNS) * WINDOW_HEIGHT + OK_BUTTON_OFFSET_REMOTEHOST[1]
        click_ok_and_reconnect(ok_x, ok_y)
        time.sleep(2.0)
    else:
        time.sleep(2.0)
