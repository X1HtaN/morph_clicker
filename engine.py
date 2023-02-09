import db_settings
import gui_helper
import time
import threading
class Game:
    _money = db_settings.get_money_fromDB()
    _multiply = db_settings.get_multiply_fromDB()
    _run = True
    
    def __init__(self):
        self.t1 = threading.Thread(target=self.conclusion_resource)
        self.t2 = threading.Thread(target=self.addition)
        self.t1.start()
        self.t2.start()

    def conclusion_resource(self):
        while self._run:
            gui_helper.conclusion_resource_fromDB()

    def addition(self):
        while self._run:
            __class__._money += __class__._multiply
            time.sleep(1)

    def save_fromGame(self):
        return [self._money, self._multiply]

    def info(self):
        return f"{self._money} {self._multiply}"