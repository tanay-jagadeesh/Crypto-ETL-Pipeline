import sqlite3

database = sqlite3.connect('crypto.db')

c = database.cursor()

# c.execute("""
#     CREATE TABLE IF NOT EXISTS prices (
#         coin TEXT,
#         price_usd REAL,
#         timestamp TEXT
#     )
# """)

c.execute("INSERT INTO prices VALUES ('bitcoin', 27345.67, '2025-09-24 20:15:00')")

c.execute("SELECT * FROM prices WHERE price_usd = 'bitcoin'")

print(c.fetchone())


database.commit()

database.close()