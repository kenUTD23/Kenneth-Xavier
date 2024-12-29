import sqlite3


def connect_db():
    con = sqlite3.connect('expense_tracker.db')
    cur = con.cursor()
    return con, cur

def initialize_db():
    con, cur = connect_db()
    cur.execute('''CREATE TABLE IF NOT EXISTS categories (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FOOD INTEGER DEFAULT 0,
    MISC INTEGER DEFAULT 0,
    UBER INTEGER DEFAULT 0,
    OTHER INTEGER DEFAULT 0)''')

    con.commit()
    con.close()



def insert_expense(category, amount):
    con, cur = connect_db()

    if category == "Food":
        cur.execute("UPDATE categories SET FOOD = FOOD + ? WHERE ID = 1", (amount,))
    elif category == "Misc":
        cur.execute("UPDATE categories SET MISC = MISC + ? WHERE ID = 1", (amount,))
    elif category == "Uber":
        cur.execute("UPDATE categories SET UBER = UBER + ? WHERE ID = 1", (amount,))
    elif category == "Other":
        cur.execute("UPDATE categories SET OTHER = OTHER + ? WHERE ID = 1", (amount,))
    else:
        print("Invalid category")
        return

    con.commit()
    con.close()

def view_expenses():
    con, cur = connect_db()
    cur.execute("SELECT * FROM categories")
    views = cur.fetchall()
    columns = ['ID', 'Food', 'Misc', 'Uber', 'Other']
    for view in views:
        print(
            f"{columns[0]}: {view[0]}, {columns[1]}: {view[1]}, {columns[2]}: {view[2]}, {columns[3]}: {view[3]}, {columns[4]}: {view[4]}")
    con.close()

def get_category_total(category):
    con, cur = connect_db()
    query = f"SELECT {category} FROM categories"
    cur.execute(query)
    results = cur.fetchall()
    total = sum(row[0] for row in results)
    return total


def monthly_total():
    con, cur = connect_db()
    query = "SELECT * FROM categories"
    cur.execute(query)

    rows = cur.fetchall()

    month_total = 0
    for row in rows:
        total_for_row = sum(row[1:])
        month_total += total_for_row

    print(f"The overall monthly total is {month_total}")
    con.close()