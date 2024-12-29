from tkinter import *
import main  # Import your main logic

def add_expense_gui():
    def submit_expense():
        category = category_input.get()
        amount = amount_input.get()
        if amount.isdigit():
            main.add_expense(category, float(amount))  # Call the backend function
            result_label.config(text=f"Added {amount} to {category}")
        else:
            result_label.config(text="Invalid amount entered")

    # Create a new window for adding expenses
    add_window = Toplevel(root)
    add_window.title("Add Expense")
    add_window.geometry("400x300")
    Label(add_window, text="Category:").pack(pady=10)
    category_input = Entry(add_window)
    category_input.pack(pady=5)
    Label(add_window, text="Amount:").pack(pady=10)
    amount_input = Entry(add_window)
    amount_input.pack(pady=5)
    Button(add_window, text="Submit", command=submit_expense).pack(pady=20)
    result_label = Label(add_window, text="")
    result_label.pack()

def view_expenses_gui():
    # Create a new window to display expenses
    view_window = Toplevel(root)
    view_window.title("View Expenses")
    view_window.geometry("400x300")
    expenses = main.view_expenses()  # Call the backend function
    Label(view_window, text="Expenses:").pack(pady=10)
    expense_text = Text(view_window, height=15, width=40)
    expense_text.pack()
    expense_text.insert(END, expenses)
    expense_text.config(state=DISABLED)

def category_total_gui():
    def show_total():
        category = category_input.get()
        total = main.category_total(category)  # Call the backend function
        result_label.config(text=f"Total for {category}: {total}")

    # Create a new window for category total
    total_window = Toplevel(root)
    total_window.title("Category Total")
    total_window.geometry("400x300")
    Label(total_window, text="Category:").pack(pady=10)
    category_input = Entry(total_window)
    category_input.pack(pady=5)
    Button(total_window, text="Show Total", command=show_total).pack(pady=20)
    result_label = Label(total_window, text="")
    result_label.pack()

def monthly_total_gui():
    # Create a new window for displaying the monthly total
    total_window = Toplevel(root)
    total_window.title("Monthly Total")
    total_window.geometry("400x200")
    
    # Call the backend function to get the total
    total = main.monthly_total()
    
    # Display the result in the new window
    result_label = Label(total_window, text=f"Monthly Total: {total}", font=("Helvetica", 14))
    result_label.pack(pady=20)


# Main GUI
root = Tk()
root.title("Expense Tracker")
root.configure(bg="grey")

Button(root, text="Add Expense", width=30, height=5, bg="gold", command=add_expense_gui).place(x=20, y=300)
Button(root, text="Category Total", width=30, height=5, bg="gold", command=category_total_gui).place(x=320, y=300)
Button(root, text="View Expense", width=30, height=5, bg="gold", command=view_expenses_gui).place(x=620, y=300)
Button(root, text="Monthly Total", width=30, height=5, bg="gold", command=monthly_total_gui).place(x=920, y=300)

# Set window size
root.geometry("1200x800")
root.mainloop()
