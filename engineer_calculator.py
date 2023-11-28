from tkinter import Tk, END, messagebox, ttk, W, E, N, S
import math

def calc(key):
    try:
        if key == '=':
            expression = calc_entry.get()
            # Replace '÷' with '/'
            expression = expression.replace('÷', '/')
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
            calc_entry.delete(0, END)
        elif key == 'Exit':
            root.after(1, root.destroy)
        else:
            # For other keys, insert them into the entry
            calc_entry.insert(END, key)
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        calc_entry.delete(0, END)
        calc_entry.insert(END, 'Error')
        messagebox.showerror('Error', str(e))

def perform_unary_operation(operation, value):
    if operation == 'cos':
        return math.cos(float(value))
    elif operation == 'sin':
        return math.sin(float(value))
    elif operation == 'log':
        return math.log10(float(value))
    elif operation == 'ln':
        return math.log(float(value))
    elif operation == 'n!':
        return math.factorial(int(value))
    elif operation == 'e':
        return math.e
    elif operation == 'π':
        return math.pi
    elif operation == '√':
        return math.sqrt(float(value))

root = Tk()
root.title('Инженерный калькулятор')
root.configure(bg='#CCCCCC')  #Gray background

# Styling
style = ttk.Style()
style.configure("TButton", padding=(10, 5), font=('Arial', 12))
style.configure("TEntry", font=('Arial', 14))

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
    '4', '5', '6', 'xⁿ', '%',
    '1', '2', '3', '(', ')',
    '0', '.', '=', 'C', 'Exit'
]

calc_entry = ttk.Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5, sticky=W + E + N + S, pady=10)

r = 1
c = 0
for btn in btn_list:
    rel = ''
    cmd = lambda x=btn: calc(x)

    ttk.Button(root, text=btn, command=cmd).grid(row=r, column=c, pady=5, sticky=W + E + N + S)
    c += 1
    if c > 4:
        c = 0
        r += 1
#start
root.mainloop()
