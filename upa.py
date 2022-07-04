
import pyautogui as pg
import pyperclip

def type_drug(drug,consumption,first):
    pyperclip.copy(drug)
    pg.hotkey('alt','5')
    if first == True: pg.click(x=866,y=305)
    if first == False: pg.click(x=759,y=323) 
    pg.hotkey('ctrl','a')
    pg.press('Backspace')
    pg.hotkey('ctrl','v')
    pg.press('Backspace',2)
    pg.sleep(1)
    if first == True: 
        pg.click(866,333,duration=1)
        pg.click(x=410,y=412)
    if first == False: 
        pg.click(721,350,duration=1)
        pg.click(x=447,y=414)
    pg.hotkey('ctrl','a')
    pg.press('Backspace')
    pg.typewrite(consumption)
    #pg.press('enter')

def openupa():
    pg.hotkey('alt','5')
    pg.sleep(1)
    pg.hotkey('alt','d')
    pg.typewrite('chromium')
    pg.press('enter')
    pg.sleep(3)
    pg.hotkey('ctrl','L')
    pg.typewrite('https://sc.upa.gov.eg/')
    pg.press('enter')