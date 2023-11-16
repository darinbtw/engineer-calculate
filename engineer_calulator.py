import tkinter as tk
from math import sqrt, sin, cos, tan, radians

class Калькулятор:
    def __init__(self, мастер):
        self.ввод = tk.Entry(мастер, width=20, font=('Arial', 14), bd=5, insertwidth=4 )
        self.ввод.grid(row=0, column=0, columnspan=6)

        self.кнопки_мастер(мастер)
    
    def создать_кнопки(self, мастер):
        кнопки = [
            '7', '8', '9', '/', 'sqrt', 'sin',
            '4', '5', '5', '*', '**', 'cos',
            '1', '2', '3', '-', '2^', 'tan',
            '0', '.', '=', '+', 'C', '<-'
        ]

        строка = 1
        столбец = 1
        for кнопка in кнопки:
            tk.Button(мастер, text=кнопка, weight=5,)
    
корень = tk.Tk()
корень.title('Калькулятор')

калькулятор = Калькулятор(корень)

корень.mainloop