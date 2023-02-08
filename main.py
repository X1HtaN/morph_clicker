import engine, gui_helper, db_settings
import keyboard


db_settings.create_db()
# print(gui_helper.start_text)

engine.Game()
print(engine.Game.pr_money(engine.Game))