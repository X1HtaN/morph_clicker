import engine as en, gui_helper, db_settings
import keyboard
import os

#hotkey functions
def end():
    db_settings.save_db()
    en.Game._run = False

def rain_drop():
    if en.Game._money >= 20:
        en.Game._multiply += 2
        en.Game._money -= 20
        db_settings.plus_item(0)

def clarity():
    if en.Game._money >= 200:
        en.Game._multiply += 10
        en.Game._money -= 200
        db_settings.plus_item(1)

def bottle():
    if en.Game._money >= 1000:
        en.Game._multiply += 50
        en.Game._money -= 1000
        db_settings.plus_item(2)

def power_threads():
    if en.Game._money >= 5000:
        en.Game._multiply += 250
        en.Game._money -= 5000
        db_settings.plus_item(3)

def manta():
    if en.Game._money >= 15000:
        en.Game._multiply += 1000
        en.Game._money -= 15000
        db_settings.plus_item(4)

def skadi():
    if en.Game._money >= 55000:
        en.Game._multiply += 3800
        en.Game._money -= 55000
        db_settings.plus_item(5)

def satanik():
    if en.Game._money >= 120000:
        en.Game._multiply += 6000
        en.Game._money -= 120000
        db_settings.plus_item(6)

def aegis():
    if en.Game._money >= 800000:
        en.Game._multiply += 40000
        en.Game._money -= 800000
        db_settings.plus_item(7)

def win():
    if en.Game._money >= 10000000:
        en.Game._run = False
        zeroing()
        print("You destroy ancient")

def zeroing():
    en.Game._money = 1
    en.Game._multiply = 1
    db_settings.plus_item(999999)

#create DB
db_settings.create_db()

#hotkeys
keyboard.add_hotkey("ctrl + Q", end)
keyboard.add_hotkey("ctrl + 1", rain_drop)
keyboard.add_hotkey("ctrl + 2", clarity)
keyboard.add_hotkey("ctrl + 3", bottle)
keyboard.add_hotkey("ctrl + 4", power_threads)
keyboard.add_hotkey("ctrl + 5", manta)
keyboard.add_hotkey("ctrl + 6", skadi)
keyboard.add_hotkey("ctrl + 7", satanik)
keyboard.add_hotkey("ctrl + 8", aegis)
keyboard.add_hotkey("ctrl + 9", win)
keyboard.add_hotkey("ctrl + z", zeroing)

#start Game
en.Game()