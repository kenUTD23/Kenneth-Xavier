import json
import  database


Expenses = {'Food': [],
            'Uber': [],
            'Other': [],
            'Lent': []
            }


def add_expense(category, amount):
    category = category.title()
    if category in Expenses:
        database.insert_expense(category, amount)
        Expenses[category].append(amount)
        print(f'{amount} is added to {category}')
    else:
        print('That is not a valid expense')



def view_expenses():
    database.view_expenses()


def category_total(category):
    category = category.title()
    if category in Expenses:
        total = database.get_category_total(category)
        print(f"The total for {category} is {total}")
    else:
        print(f"{category} is not a valid category")


def monthly_total():
    database.monthly_total()


def save_expenses():
    with open('expenses.json', 'w', encoding='utf-8') as file:
        json.dump(Expenses, file, ensure_ascii=False, indent=4)
        print("Expenses have been saved")

database.initialize_db()