import db_settings
import gui_helper
import time
class Game:
    _money = db_settings.get_money_fromDB()
    _multiply = db_settings.get_multiply_fromDB()
    _run = True

    def __new__(self):
        self.run(__class__)

    def run(self):
        while self._run == True:
            __class__._money += __class__._multiply
            gui_helper.conclusion_resource()
            time.sleep(1)

    def save_fromGame(self):
        return [self._money, self._multiply]

    def info(self):
        return f"{self._money} {self._multiply}"