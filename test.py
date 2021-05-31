import sqlite3 as db

connection_obj = db.connect("expenseTracker.db")

curr = connection_obj.cursor()
query = """
SELECT name, title, date, expense FROM expenses ORDER BY name
"""

curr.execute(query)
rows = curr.fetchall()
print(rows)
