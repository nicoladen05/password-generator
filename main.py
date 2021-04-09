from random import choice
import tkinter as tk
import base64
from functools import partial

class Generator:

    def __init__(self, characters, capitals, numbers, symbols):
        self.characters = characters
        self.capitals = capitals
        self.numbers = numbers
        self.symbols = symbols
        self.template = ''

        if self.characters:
            self.template = self.template + 'abcdefghijklmnopqrstuvwxyz'
        
        if self.capitals:
            self.template = self.template + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        if self.numbers:
            self.template = self.template + '1234567890'

        if self.symbols:
            self.template = self.template + '~!@#$§%&*?'
        
    def generate(self, length):
        self.length = length
        self.password = ''

        for i in range(self.length):
            self.password = self.password + choice(self.template)
        
        return self.password

def save_value(val):
    global length
    length = int(val)

def password():
    global charactes
    global capitals
    global numbers
    global symbols
    global length
    global output
    global passtxt

    charactes_bool = bool()
    capitals_bool = bool()
    numbers_bool = bool()
    symbols_bool = bool()

    if charactes.get() == 1:
        charactes_bool = True

    if capitals.get() == 1:
        capitals_bool = True

    if numbers.get() == 1:
        numbers_bool = True

    if symbols.get() == 1:
        symbols_bool = True

    try:
        g = Generator(charactes_bool, capitals_bool, numbers_bool, symbols_bool)
        passtxt = g.generate(length)
        output.config(text = passtxt)
    except IndexError:
        output.config(text = 'Select at least one checkbox')

def copy():
    global passtxt

    win.clipboard_clear()
    win.clipboard_append(passtxt)


win = tk.Tk()
win.title('Password Generator')
win.geometry('250x250')
win.resizable(True, True)
win.configure(bg='#f9f6ec')

length = 1
passtxt = 'Not Generated Yet'
charactes = tk.IntVar()
capitals = tk.IntVar()
numbers = tk.IntVar()
symbols = tk.IntVar()


cb_charactes = tk.Checkbutton(win, text='Characters', bg = '#f9f6ec', fg = '#0d0c0c', variable=charactes).pack()
cb_capitals = tk.Checkbutton(win, text='Capitals', bg = '#f9f6ec', fg = '#0d0c0c', variable=capitals).pack()
cb_numbers = tk.Checkbutton(win, text='Numbers', bg = '#f9f6ec', fg = '#0d0c0c', variable=numbers).pack()
cb_symbols = tk.Checkbutton(win, text='Symbols', bg = '#f9f6ec', fg = '#0d0c0c', variable=symbols).pack()
        
length_slider = tk.Scale(win, from_ = 1, to = 100, orient = 'horizontal', command = save_value).pack()

output = tk.Label(win, text=passtxt, bg = '#f9f6ec', fg = '#88a1a8')

generate = tk.Button(win, text="Generate!", bg = '#88a1a8', fg = '#0d0c0c', command = password).pack()

output.pack()

copy = tk.Button(win, text="Copy to clipboard", command = copy).pack()

win.mainloop()
