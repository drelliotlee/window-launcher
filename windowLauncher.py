'''
This program open's up all my most common websites/windows and moves them
into the positions I like, so I can start being productive right away
'''

import subprocess
import win32gui
import time
import os
import re

def moveWindowByWildcard(hwnd, tup):
	'''
	tup[0] is wildcard
	tup[0] is x
	tup[0] is y
	tup[0] is width
	tup[0] is height
	'''
	if tup[0] in win32gui.GetWindowText(hwnd):
		win32gui.MoveWindow(hwnd, tup[1], tup[2], tup[3], tup[4], True)

subprocess.Popen(
	[r"C:\Program Files\Google\Chrome\Application\chrome.exe",
	'-app=https://ticktick.com/webapp/#p/63b6330c8f08f73ded0afb78/tasks/63b63d8f56148929e0849496'],
	)
subprocess.Popen(
	[r"C:\Program Files\Google\Chrome\Application\chrome.exe",
	f'--app=https://mail.google.com/mail/u/0/?shva=1#inbox'])
subprocess.Popen(
	[r"C:\Program Files\Google\Chrome\Application\chrome.exe",
	f'--app=https://chat.openai.com/chat'])
subprocess.call(
	[r"C:\Windows\explorer.exe",
	r"C:\Users\Elliot\Desktop"],
	shell=True)
subprocess.call(
	[r"C:\Users\Elliot\AppData\Local\Programs\Microsoft VS Code\Code.exe"])
subprocess.call(
	["start",
	r"C:\Users\Elliot\AppData\Local\Obsidian\Obsidian.exe"],
	shell=True)
subprocess.call(
	[r"C:\Program Files\Google\Chrome\Application\chrome.exe"])

#EnumWindows is like a 'for loop' for the win32gui package.
# it runs the function on every window, along with the provided 2nd argument
win32gui.EnumWindows(moveWindowByWildcard, ('TickTick',4049, 0, 438, 1059))
win32gui.EnumWindows(moveWindowByWildcard, ('Gmail',3214, 0, 849, 462))
win32gui.EnumWindows(moveWindowByWildcard, ('New Chat',2553, 0, 675, 1057))
win32gui.EnumWindows(moveWindowByWildcard, ('Desktop',3214, 455, 849, 602))
win32gui.EnumWindows(moveWindowByWildcard, ('Visual Studio Code',0,0,728,1050))
win32gui.EnumWindows(moveWindowByWildcard, ('Obsidian',1797,0,763,1050))
win32gui.EnumWindows(moveWindowByWildcard, ('New Tab',721,0,1083,1057))

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
#             print("Window %s:" % win32gui.GetWindowText(hwnd))
#             print("\tLocation: (%d, %d)" % (x, y))
#             print("\t    Size: (%d, %d)" % (w, h))
# win32gui.EnumWindows(callback, None)