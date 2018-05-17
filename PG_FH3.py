import time
import pyautogui as pg


pg.hotkey('f1')
pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n', .3)
pg.hotkey('winleft','up')
pg.typewrite('https://www.youtube.com/watch?v=8YGlzSl6cxU\n'.3)
time.sleep(1)
for x in range(0,51):
    pg.hotkey('f3')
pg.hotkey('winleft','tab')
for x in range(0,10):
    pg.hotkey('ctrl','winleft','left')
