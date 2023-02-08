import db_settings
class Game:
    _money = db_settings.get_money()

    def __init__(self):
        pass

    def pr_money(self):
        return self._money