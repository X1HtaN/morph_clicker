import engine, gui_helper, db_settings
import keyboard
import os

#hotkey functions
def end():
    db_settings.save_db()
    engine.Game._run = False

def test_buy():
    engine.Game._multiply += 10

def zeroing():
    engine.Game._money = 1
    engine.Game._multiply = 1

#create DB
db_settings.create_db()

#hotkeys
keyboard.add_hotkey("ctrl + Q", end)
keyboard.add_hotkey("ctrl + 1", test_buy)
keyboard.add_hotkey("ctrl + 0", zeroing)

#start Game
engine.Game()