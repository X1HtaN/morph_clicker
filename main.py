import engine, gui_helper, db_settings
import keyboard

#hotkey functions
def end():
    db_settings.save_db()
    engine.Game._run = False

#create DB
db_settings.create_db()

#hotkeys
keyboard.add_hotkey("ctrl + Q", end)

#start Game
# print(gui_helper.start_text)
engine.Game()
# print(engine.Game.info(engine.Game))