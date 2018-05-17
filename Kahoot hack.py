import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.3)
pg.hotkey('winleft','up')
pg.typewrite('https://www.youtube.com/watch?v=8YGlzSl6cxU\n',.001)
time.sleep(1)
