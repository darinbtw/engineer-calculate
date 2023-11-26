from tkinter import Tk, END, messagebox, ttk, W, E, N, S

import math

root = Tk()
root.title('Инженерный калькулятор')

# Устанавливаем веса для автоматического изменения размеров при изменении окна
for i in range(5):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

# Устанавливаем минимальный размер окна
root.minsize(width=400, height=500)

btn_list = [
    'cos', 'sin', 'log', 'ln', 'n!',
    'e', 'π', '√', '+', '*',
    '7', '8', '9', '-', '÷',
    '4', '5', '6', 'xⁿ', '%',
    '1', '2', '3', '(', ')',
    '0', '.', '=', 'C', 'Exit'
]

calc_entry = ttk.Entry(root, width=33, font=('Arial', 14))
calc_entry.grid(row=0, column=0, columnspan=5, sticky=W + E + N + S, pady=10)

ttk.Style().configure("TButton", padding=(0, 10, 0, 10), font=('Arial', 12))

r = 1
c = 0
for btn in btn_list:
    rel = ''
    cmd = lambda x=btn: calc(x)

    ttk.Button(root, text=btn, command=cmd, width=15).grid(row=r, column=c, pady=5, sticky=W + E + N + S)
    c += 1
    if c > 4:
        c = 0
        r += 1

def calc(key):
    if key == '=':
        try:
            expression = calc_entry.get()
            result = eval(expression)
            calc_entry.delete(0, END)
            calc_entry.insert(END, str(result))
        except ValueError:
            calc_entry.delete(0, END)
            calc_entry.insert(END, 'Ошибка!')
            messagebox.showerror('Ошибка! Проверьте введенные данные.')
    elif key == 'cos':
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == 'sin':
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == 'log':
        calc_entry.insert(END, "=" + str(math.log(int(calc_entry.get()))))
    elif key == 'ln':
        calc_entry.insert(END, "=" + str(math.log(int(calc_entry.get()), math.e)))
    elif key == 'n!':
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
    elif key == 'e':
        calc_entry.insert(END, math.e)
    elif key == 'π':
        calc_entry.insert(END, math.pi)
    elif key == '√':
        calc_entry.insert(END, '=' + str(math.sqrt(int(calc_entry.get()))))
    elif key == '÷':
        calc_entry.insert(END, '/')
    elif key == 'xⁿ':
        calc_entry.insert(END, '**')
    elif key == '(':
        calc_entry.insert(END, '(')
    elif key == ')':
        calc_entry.insert(END, ')')
    elif key == 'C':
        calc_entry.delete(0, END)
    elif key == 'Exit':
        root.after(1, root.destroy)
    else:
        calc_entry.insert(END, key)

root.mainloop()
