import tkinter as tk
from math import sqrt, sin, cos, tan, radians, log, log10, exp, radians
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        #self.ввод вводим , потом widht(ширина), font('Arial, это шрифт', bd(ширина ввода), insertwidth(ширина вставки),valide(key(проверяет на ввод именно чисел в поле для ввода)), validatecommand(связывает функцию))
        self.ввод = tk.Entry(master, width=20, font=('Arial', 14), bd=30, insertwidth=4, validate='key', validatecommand=(master.register(self.проверка_ввода), '%P' ))
        #grid(графическая сетка)(ввод=tk.Entry),row(с какой столбец начинается,column(с какой строчки),columnspan(Сколько виджетов будет добавлено))
        self.ввод.grid(row=0, column=0, columnspan=4,padx=10, pady=10, sticky='nsew')# padx, pady=расширение по всем сторонам,sticky=n(север)s(юг),запад и восток.nsew
        #создаем графические кнопки с помощью переменной создать кнопки в главной команде(окно)
        self.создать_кнопки(master)
        #стиль кнопок(тематика стиля)
        стиль = ttk.Style()
        #стиль кнопок и размер этих кнопок
        стиль.configure('TButton', font=('Arial', 14))

        self.создать_кнопки(master)
        #Когда интерфейс растягиваешь и кнопки тоже растягиваются
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # Когда нажимаешь на кнопку идёт обработка клавишь
        master.bind('<Key>', self.обработать_клавишу)
    #создаем новый блок с проверкой вводка
    #self(сам)
    def проверка_ввода(self, symbols):
        # Разрешаем вводить только цифры, знаки операций и другие разрешенные символы
        разрешенные_символы = set("0123456789+-*/.C←=sqrtsincostanlnlog10exp")
        #прверяет символы если их нет в 30 строчке кода, то ничего не пишеться, all= проверяет есть ли буква/цифра в переменной
        return all(c in разрешенные_символы for c in symbols)
    #Создаем отдельный блок схемы с графическими кнопками с которыми мы будем функциионировать
    def создать_кнопки(self, master):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+', 
            'C', '<-',
            'sqrt', 'sin', 'cos', 'tan',
            'ln', 'log', 'exp',
        ]
        #Строка и столбец это изначальные переменные, с которыми мы будем менять кнопки или интерфейс
        line = 1
        column1 = 0
        #Это цикл, который перебирает каждую кнопку из списка кнопки.
        for button in buttons:
            #ttk.button=современный интерфейс кнопок
            #Кнопка имеет текст кнопка, ширину 5, а также связана с методом self.нажата_кнопка, который вызывается при нажатии кнопки. padx=5, pady=5 добавляют внутренние отступы, а sticky='nsew' указывает на растягивание кнопки во всех направлениях.
            #command=lambda = связывает функции с нажатием кнопок
            ttk.Button(master, text=button, width=5, command=lambda б=line: self.нажата_кнопка(б)).grid(row=line, column=column1, padx=5, pady=5, sticky='nsew')
            master.columnconfigure(column1, weight=1)
            column1 += 1
            if column1 > 3:
                column1 = 0
                line += 1 
    #создаем блок схему, если нажата кнопка
    #если нажата ("кнопка") self(сам).значение кнопки
    def нажата_кнопка(self, meaning):
        if meaning == '=':
            self.вычислить()
        elif meaning == 'C':
            self.очистить_ввод()#ставим ()чтобы это посчитало как ничего и просто то что там записано стриалось
        elif meaning == 'c':
            self.очистить_ввод()#ставим ()чтобы это посчитало как ничего и просто то что там записано стриалось
        elif meaning == '<-':
            self.backspace()#ставим ()чтобы это посчитало как ничего и просто то что там записано стриалось
        else:
            self.добавить_к_вводу(meaning) #Добавление к вводу(значение)

    def обработать_клавишу(self, event):
        клавиша = event.char
        if клавиша == '\r':
            клавиша = '='  # клавиша "Enter" будет использоваться как "="
        elif event.keysym == 'BackSpace':
            self.backspace()
            return
        self.нажата_кнопка(клавиша)

    def вычислить(self):
        try:
            выражение = self.ввод.get()

            # Заменим символы ln, log10 и exp соответствующими функциями из библиотеки math
            выражение = выражение.replace('ln', 'log')
            выражение = выражение.replace('log10', 'log10')
            выражение = выражение.replace('exp', 'exp')

            результат = str(eval(выражение))
            self.очистить_ввод()
            self.вставить_в_ввод(str(результат))
        except Exception as e:
            self.очистить_ввод()
            self.вставить_в_ввод("Ошибка")

    def очистить_ввод(self):
        self.ввод.delete(0, tk.END)

    def вставить_в_ввод(self, значение):
        self.ввод.insert(tk.END, значение)

    def добавить_к_вводу(self, значение):
        текущее = self.ввод.get()
        self.очистить_ввод()
        self.вставить_в_ввод(str(текущее) + str(значение))

    def backspace(self):
        текущее = self.ввод.get()[:-1]
        self.очистить_ввод()
        self.вставить_в_ввод(текущее)

start = tk.Tk()
start.title("Engineer Calculator")

калькулятор = Calculator(start)

start.mainloop()