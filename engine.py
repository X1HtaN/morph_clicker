import db_settings
class Game:
    _money = db_settings.get_money()
    _multiply = db_settings.get_multiply()

    def __init__(self):
        pass

    def info(self):
        return f"{self._money} {self._multiply}"