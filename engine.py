import db_settings
class Game:
    _money = db_settings.get_money_fromDB()
    _multiply = db_settings.get_multiply_fromDB()
    _run = True

    def __init__(self):
        self.run()

    def run(self):
        while self._run == True:
            pass

    def save_fromGame(self):
        self._money += 1000
        self._multiply += 20
        return [self._money, self._multiply]

    def info(self):
        return f"{self._money} {self._multiply}"