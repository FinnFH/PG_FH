import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.3)
pg.hotkey('winleft','up')
pg.typewrite('mail.google.com/mail/u/0/#inbox\n',.001)
time.sleep(1)
pg.moveTo(557, 688,.1)
pg.click()
time.sleep(1)
pg.moveTo(467, 316,.1)
pg.click()
for x in range (0,10):
    pg.hotkey('ctrl','winleft','left')

