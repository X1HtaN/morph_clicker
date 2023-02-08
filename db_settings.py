import sqlite3 as sq

def create_db():
    with sq.connect("data.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS resources (
            money INTEGER NOT NULL DEFAULT 1,
            multiply INTEGER NOT NULL DEFAULT 1,
            up1 INTEGER NOT NULL DEFAULT 1,
            up2 INTEGER NOT NULL DEFAULT 1,
            up3 INTEGER NOT NULL DEFAULT 1,
            up4 INTEGER NOT NULL DEFAULT 1,
            up5 INTEGER NOT NULL DEFAULT 1,
            up6 INTEGER NOT NULL DEFAULT 1,
            up7 INTEGER NOT NULL DEFAULT 1,
            up8 INTEGER NOT NULL DEFAULT 1,
            up9 INTEGER NOT NULL DEFAULT 1,
            up10 INTEGER NOT NULL DEFAULT 1
        )""")

def get_money():
    with sq.connect("data.db") as con:
        cur = con.cursor()

        cur.execute("""SELECT money FROM resources""")
        for i in cur:
            return i[0]

# def test():
#     with sq.connect("data.db") as con:
#         cur = con.cursor()

#         cur.execute("""UPDATE resources SET money = money + 500""")