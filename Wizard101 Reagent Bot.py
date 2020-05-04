import time 
import subprocess as sub
import pyautogui as pyauto
import os

# This asks for the Item you want to find in the bazzar
# Make sure your on 800x600 and make the interface as big as possible
print("Before entering anything, move this terminal out of the way of the games window\nMake sure to have a png screenshot of the Item you will be hunting down, This has to be in the same directory\n\n")


# Asking for information and setting mode to buying one each time, all, or half
Item = input('What Item do you need?\n')
Amount = int(input('How many do you need?\n'))
Buy_All = input("Buy all mode? pick yes, no, or half\n")
if Buy_All == 'yes':
    def Buying_All():
        print(" ")
        pyauto.dragRel(xOffset=200, mouseDownUp=True, duration=0.5)
else:
    pass
if Buy_All == 'no':
    def Buying_All():
        print(" ")
else:
    pass
if Buy_All == 'half':
    def Buying_All():
        print(" ")
        pyauto.dragRel(xOffset=60, mouseDownUp=True, duration=0.5)
else:
    pass
print('Getting Item: ' + Item)
Item = (Item + ".png")


# This will press X on the Elick Silverfistbbx
time.sleep(3)
pyauto.click(x=95, y=30)
pyauto.click()
time.sleep(1)
pyauto.press('x')


# We are in the book and now being taken to the Reagents section
time.sleep (0.3)
pyauto.moveTo(x=750, y=135)
time.sleep (0.3)
pyauto.click()
pyauto.click()
pyauto.click()
time.sleep(4)


# Item picture that will be targeted
Search_And_Destroy = pyauto.locateOnScreen(Item)
SAD = Search_And_Destroy


# Amount = How many times this will loop around
Looper = 0
while Looper < Amount:
    Looper = Looper + 1
    while SAD == None:
        pyauto.moveTo(x=630, y=520)
        SAD=pyauto.locateOnScreen(Item)
        if SAD != None:
            continue
        pyauto.click()
        SAD=pyauto.locateOnScreen(Item)
        if SAD != None:
            continue
        pyauto.click()
        SAD=pyauto.locateOnScreen(Item)
        if SAD != None:
            continue
        pyauto.click()
        SAD=pyauto.locateOnScreen(Item)
        if SAD != None:
            continue
        pyauto.click()
        SAD=pyauto.locateOnScreen(Item)
        if SAD != None:
            continue
        pyauto.click()
        SAD=pyauto.locateOnScreen(Item)
        if SAD != None:
            continue
        pyauto.click()
        SAD=pyauto.locateOnScreen(Item)
        if SAD != None:
            continue
        pyauto.moveTo(x=50, y=130)
        pyauto.click()
        time.sleep(2)

    # Item Found
    Item_Found = pyauto.center(SAD)
    pyauto.moveTo(Item_Found)
    pyauto.click(Item_Found)

    # Buying the Item
    pyauto.moveTo(x=100, y=550)
    pyauto.click()
    pyauto.moveTo(x=523, y=400)
    pyauto.moveTo(x=400, y=400)
    time.sleep(0.5)
    
    # Dragging Mouse
    Buying_All()
    pyauto.moveTo(x=300, y=540)
    pyauto.click()

    # Clicking Buy Button
    time.sleep(3)
    pyauto.moveTo(x=520, y=400)
    pyauto.click()
    Looper = str(Looper)
    print(Looper + " Obtained")
    Looper = int(Looper)
    time.sleep(1)
    pyauto.moveTo(x=50, y=130)
    pyauto.click()
    SAD = None


# Finished and closing book
time.sleep(2)
pyauto.moveTo(x=760, y=580)
pyauto.click()
print("\nItems have been obtained enjoy :^)")
