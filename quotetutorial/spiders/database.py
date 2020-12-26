import sqlite3

conn = sqlite3.connect("quote.db")
curr = conn.cursor()

'''curr.execute("""create table quote_tb(
    title text,
    author text,
    tag text)""")'''

curr.execute("""insert into quote_tb values ("Akash", "Chidanand", "yadaouda")""")

conn.commit()
conn.close()


