import sqlite3 as db


def init():
    connection_obj = db.connect("expenseTracker.db")
    curr = connection_obj.cursor()
    query = """
    create table if not exists expenses (
        date string,
        name string,
        title string,
        expense number,
        state string
        )
    """
    curr.execute(query)
    connection_obj.commit()


def submit_expense(name, title, expense, date, state):
    connection_obj = db.connect("expenseTracker.db")
    curr = connection_obj.cursor()
    query = """
    INSERT INTO expenses VALUES 
    (?, ?, ?, ?, ?)
    """
    curr.execute(query, (date, name, title, expense, state))
    connection_obj.commit()


def view_expense():
    connection_obj = db.connect("expenseTracker.db")
    curr = connection_obj.cursor()
    query = """
     select name, title, expense, date, state from expenses ORDER BY name
    """
    total = """
    select sum(expense) from expenses
    """
    curr.execute(query)
    rows = curr.fetchall()
    curr.execute(total)
    amount = curr.fetchall()[0]

    return rows, amount[0]


def group_by_name():
    connection_obj = db.connect("expenseTracker.db")
    curr = connection_obj.cursor()
    query = """
    SELECT name, SUM(expense) FROM expenses GROUP BY name ORDER BY name
    """
    curr.execute(query)
    rows = curr.fetchall()
    return rows


def group_by_title():
    connection_obj = db.connect("expenseTracker.db")
    curr = connection_obj.cursor()
    query = """
    SELECT title, SUM(expense) FROM expenses GROUP BY title ORDER BY title
    """
    curr.execute(query)
    rows = curr.fetchall()
    return rows


def group_by_state():
    connection_obj = db.connect("expenseTracker.db")
    curr = connection_obj.cursor()
    query = """
    SELECT state, SUM(expense) FROM expenses GROUP BY state ORDER BY state
    """
    curr.execute(query)
    rows = curr.fetchall()
    return rows
