import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.input = tk.Entry(master, width=20, font=('Arial', 14), bd=30, insertwidth=4, validate='key', validatecommand=(master.register(self.checking_the_drive), '%P'))
        self.input.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        self.create_button(master)
        Style = ttk.Style()
        Style.configure('TButton', font=('Arial', 14))
        self.create_button(master)
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        master.bind('<Key>', self.process_the_button)

    def checking_the_drive(self, symbols):
        allowed_characters = set("0123456789+-*/.C←=sqrtsincostanlnlog10exp")
        return all(c in allowed_characters for c in symbols)

    def create_button(self, master):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '<-',
            'sqrt', 'sin', 'cos', 'tan',
            'ln', 'log', 'exp',
        ]
        line = 1
        column1 = 0
        for button in buttons:
            ttk.Button(master, text=button, width=5, command=lambda б=button: self.the_button_is_pressed(б)).grid(row=line, column=column1, padx=5, pady=5, sticky='nsew')
            master.columnconfigure(column1, weight=1)
            column1 += 1
            if column1 > 3:
                column1 = 0
                line += 1
                master.rowconfigure(line, weight=1)

    def the_button_is_pressed(self, meaning):
        if meaning == '=':
            self.calcualate1()
        elif meaning in ('C', 'c'):
            self.clear_input()
        elif meaning == '<-':
            self.backspace()
        else:
            self.add_to_input(meaning)

    def process_the_button(self, event):
        key = event.char
        if key == '\r':
            key = '='
        elif event.keysym == 'BackSpace':
            self.backspace()
            return
        self.the_button_is_pressed(key)

    def calcualate1(self):
        try:
            meaning = self.input.get()
            meaning = meaning.replace('ln', 'log')
            meaning = meaning.replace('log10', 'log10')
            meaning = meaning.replace('exp', 'exp')
            score = str(eval(meaning))
            self.clear_input()
            self.add_in_input(str(score))
        except Exception as e:
            self.clear_input()
            self.add_in_input("Error")

    def clear_input(self):
        self.input.delete(0, tk.END)

    def add_in_input(self, meaning):
        self.input.insert(tk.END, meaning)

    def add_to_input(self, meaning):
        current = self.input.get()
        self.clear_input()
        self.add_in_input(str(current) + str(meaning))

    def backspace(self):
        current = self.input.get()[:-1]
        self.clear_input()
        self.add_in_input(current)

start = tk.Tk()
start.title("Engineer Calculator")

calculator = Calculator(start)

start.mainloop()
