import sqlite3 as sq
import engine

def create_db():
    with sq.connect("data.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS resources (
            money INTEGER NOT NULL DEFAULT 1,
            multiply INTEGER NOT NULL DEFAULT 1,
            up1 INTEGER NOT NULL DEFAULT 0,
            up2 INTEGER NOT NULL DEFAULT 0,
            up3 INTEGER NOT NULL DEFAULT 0,
            up4 INTEGER NOT NULL DEFAULT 0,
            up5 INTEGER NOT NULL DEFAULT 0,
            up6 INTEGER NOT NULL DEFAULT 0,
            up7 INTEGER NOT NULL DEFAULT 0,
            up8 INTEGER NOT NULL DEFAULT 0,
            up9 INTEGER NOT NULL DEFAULT 0,
            up10 INTEGER NOT NULL DEFAULT 0
        )""")

def save_db():
    with sq.connect("data.db") as con:
        cur = con.cursor()

        saves = engine.Game.save_fromGame(engine.Game)

        cur.execute(f"UPDATE resources SET money = {saves[0]}")
        cur.execute(f"UPDATE resources SET multiply = {saves[1]}")

def get_money_fromDB():
    with sq.connect("data.db") as con:
        cur = con.cursor()

        cur.execute("""SELECT money FROM resources""")

    for i in cur:
        return i[0]

def get_multiply_fromDB():
    with sq.connect("data.db") as con:
        cur = con.cursor()

        cur.execute("""SELECT multiply FROM resources""")
    for i in cur:
        return i[0]

def get_items():
    ret = []
    with sq.connect("data.db") as con:
        cur = con.cursor()

        cur.execute("""SELECT up1,up2,up3,up4,up5,up6,up7,up8,up9 FROM resources""")
    for i in cur:
        for j in i:
            ret.append(j)
    return ret

def plus_item(num):
    with sq.connect("data.db") as con:
        cur = con.cursor()

        if num == 999999:
            cur.execute(f"UPDATE resources SET up1 = 0")
            cur.execute(f"UPDATE resources SET up2 = 0")
            cur.execute(f"UPDATE resources SET up3 = 0")
            cur.execute(f"UPDATE resources SET up4 = 0")
            cur.execute(f"UPDATE resources SET up5 = 0")
            cur.execute(f"UPDATE resources SET up6 = 0")
            cur.execute(f"UPDATE resources SET up7 = 0")
            cur.execute(f"UPDATE resources SET up8 = 0")
        if num == 0:
            cur.execute(f"UPDATE resources SET up1 = up1 + 1")
        if num == 1:
            cur.execute(f"UPDATE resources SET up2 = up2 + 1")
        if num == 2:
            cur.execute(f"UPDATE resources SET up3 = up3 + 1")
        if num == 3:
            cur.execute(f"UPDATE resources SET up4 = up4 + 1")
        if num == 4:
            cur.execute(f"UPDATE resources SET up5 = up5 + 1")
        if num == 5:
            cur.execute(f"UPDATE resources SET up6 = up6 + 1")
        if num == 6:
            cur.execute(f"UPDATE resources SET up7 = up7 + 1")
        if num == 7:
            cur.execute(f"UPDATE resources SET up8 = up8 + 1")