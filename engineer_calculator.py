from tkinter import Tk, END, messagebox, ttk, W, E, N, S
import math

def calc(key):
    try:
        if key == '=':
            expression = calc_entry.get()
            # Replace '÷' with '/'
            expression = expression.replace('÷', '/')
            # Replace 'mod' with '%'
            expression = expression.replace('mod', '%')
            result = eval(expression)
            calc_entry.delete(0, END)
            calc_entry.insert(END, str(result))
        elif key in {'cos', 'sin', 'log', 'ln', 'n!', 'e', 'π', '√'}:
            # Unary operations
            expression = calc_entry.get()
            result = perform_unary_operation(key, expression)
            calc_entry.delete(0, END)
            calc_entry.insert(END, str(result))
        elif key == 'C':
            clear_entry()
        elif key == '←':  # Backspace
            backspace()
        elif key == '^':  # Exponentiation
            # Evaluate exponentiation immediately
            expression = calc_entry.get()
            base, exponent = expression.split('^')
            result = math.pow(float(base), float(exponent))
            calc_entry.delete(0, END)
            calc_entry.insert(END, str(result))
        elif key == '%':
            # Calculate percentage
            expression = calc_entry.get()
            value, percentage = expression.split('%')
            result = float(value) * float(percentage) / 100
            calc_entry.delete(0, END)
            calc_entry.insert(END, str(result))
        elif key == '.':
            # Check if there is already a dot in the current input
            current_text = calc_entry.get()
            if '.' not in current_text:
                calc_entry.insert(END, key)
        else:
            # For numeric buttons and other operations, insert them into the entry
            if calc_entry.get() == 'Error':
                clear_entry()
            calc_entry.insert(END, key)
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        calc_entry.delete(0, END)
        calc_entry.insert(END, 'Error')
        messagebox.showerror('Error', str(e))
        # After the user clicks OK, clear the entry
        clear_entry()

def clear_entry():
    calc_entry.delete(0, END)

def backspace():
    current_expression = calc_entry.get()
    calc_entry.delete(0, END)
    calc_entry.insert(END, current_expression[:-1])

def perform_unary_operation(operation, value):
    if operation == 'cos':
        # Convert degrees to radians
        return math.cos(math.radians(float(value)))
    elif operation == 'sin':
        # Convert degrees to radians
        return math.sin(math.radians(float(value)))
    elif operation == 'log':
        return math.log10(float(value))
    elif operation == 'ln':
        return math.log(float(value))
    elif operation == 'n!':
        return math.factorial(int(value))
    elif operation == 'e':
        return str(math.e)  # Convert math.e to string
    elif operation == 'π':
        return str(round(math.pi, 10))  # Round to 10 decimal places
    elif operation == '√':
        return math.sqrt(float(value))

root = Tk()
root.title('Инженерный калькулятор')
root.configure(bg='#CCCCCC')  # Set background color to gray

# Styling
style = ttk.Style()
style.configure("TButton", padding=(10, 5), font=('Arial', 12))
style.configure("TEntry", font=('Arial', 14), state='readonly')  # Set entry field state to 'readonly'

# Window Resizing
for i in range(5):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

root.minsize(width=400, height=500)

# Buttons
btn_list = [
    'cos', 'sin', 'log', 'ln', 'n!',
    'e', 'π', '√', '+', '*',
    '7', '8', '9', '-', '÷',
    '4', '5', '6', '^', '%',  # Replace 'mod' with '%'
    '1', '2', '3', '(', ')',
    '0', '.', '=', '←', 'C'  # Reversed the order
]

calc_entry = ttk.Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5, sticky=W + E + N + S, pady=10)

r = 1
c = 0
for btn in btn_list:
    rel = ''
    cmd = lambda x=btn: calc(x)

    # Change text for the '%' button
    text = '%' if btn == '%' else btn
    ttk.Button(root, text=text, command=cmd).grid(row=r, column=c, pady=5, sticky=W + E + N + S)
    c += 1
    if c > 4:
        c = 0
        r += 1

root.mainloop()
