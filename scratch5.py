import pyautogui
from time import sleep
from itertools import product
import pynput as pp
import time


clicks = []

def on_click(x, y, button, pressed):
    if pressed:
        clicks.append((x,y))

def on_scroll(x, y, dx, dy):
    listener.stop()

with pp.mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

def click(xy):
    x, y = xy
    pyautogui.click(x, y)
    sleep(.05)

print(clicks)
sleep(.05)
click(clicks.pop(0))
sleep(.5)
vscode = clicks.pop(-1)
submit = clicks.pop(-1)
n = len(clicks)
perms = [''.join(i) for i in product('01', repeat = n)]

lastperm = '1' * n
for p in perms:
    tic = time.time()
    for idx in range(n):
        if p[idx] != lastperm[idx]:
            click(clicks[idx])
    sleep(.5)
    click(submit)
    sleep(.4)
    lastperm = p