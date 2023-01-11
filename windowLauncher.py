'''
This program open's up all my most common websites/windows and moves them
into the positions I like, so I can start being productive right away
'''

import subprocess
import win32gui
import time
import os
import re

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""
    def __init__(self):
        self._handle = None

    def _window_enum_callback(self, hwnd, wildcard):
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def move_window(self, top, left, width, height):
        win32gui.MoveWindow(self._handle, top, left, width, height, True)

def createAndMoveChrome(url:str, name:str, x:int, y:int, width:int, height:int):
    subprocess.Popen([
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        f'--app={url}'
    ])
    time.sleep(2)
    w = WindowMgr()
    w.find_window_wildcard(name)
    w.move_window(x, y, width, height)


createAndMoveChrome(
    "https://ticktick.com/webapp/#p/63b6330c8f08f73ded0afb78/tasks/63b63d8f56148929e0849496",
    ".*TickTick.*",
    4049, 0, 438, 1059
)

createAndMoveChrome(
    "https://mail.google.com/mail/u/0/?shva=1#inbox",
    ".*(Gmail|Inbox).*",
    3214, 0, 849, 462
)

createAndMoveChrome(
    "https://chat.openai.com/chat",
    ".*(Just a moment|New chat).*",
    2553, 0, 675, 1057
)

subprocess.call([r"C:\Windows\explorer.exe",r"C:\Users\Elliot\Desktop"], shell=True)
time.sleep(2)
w = WindowMgr()
w.find_window_wildcard(".*Desktop.*")
w.move_window(3214, 455, 849, 602)

subprocess.call([r"C:\Users\Elliot\AppData\Local\Programs\Microsoft VS Code\Code.exe"])
time.sleep(2)
w = WindowMgr()
w.find_window_wildcard(".*Visual Studio Code.*")
w.move_window(0,0,728,1050)

subprocess.call(["start", r"C:\Users\Elliot\AppData\Local\Obsidian\Obsidian.exe"], shell=True)
time.sleep(4)
w=win32gui.FindWindow(None, 'python - Obsidian - Obsidian v1.1.9')
win32gui.MoveWindow(w, 1797,0,763,1050, True)
# w.find_window_wildcard(".*Python.*")
# w.move_window(1797,0,763,1050)

subprocess.call([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
time.sleep(2)
w = WindowMgr()
w.find_window_wildcard("New Tab")
w.move_window(0,0,728,1050)

# CODE TO FIND NAMES OF ALL OPEN WINDOWS
# import win32gui
# def winEnumHandler( hwnd, ctx ):
#     if win32gui.IsWindowVisible( hwnd ):
#         print (hex(hwnd), win32gui.GetWindowText( hwnd ))

# win32gui.EnumWindows( winEnumHandler, None )

# CODE TO FIND SIZE AND POS OF MONITORS
# import win32gui
# def callback(hwnd, extra):
#     rect = win32gui.GetWindowRect(hwnd)
#     x = rect[0]
#     y = rect[1]
#     w = rect[2] - x
#     h = rect[3] - y
#     name = win32gui.GetWindowText(hwnd)
#     if w>10: # want to ignore ghost/invisible windows
#         if len(name)>0: # want to ignore ghost/invisible windows
#             print(win32gui.GetWindowText(hwnd))
#             print("\tLocation: (%d, %d)" % (x, y))
#             print("\t    Size: (%d, %d)" % (w, h))
# win32gui.EnumWindows(callback, None)


