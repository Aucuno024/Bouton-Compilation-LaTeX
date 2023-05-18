from compile import pdflatex
import tkinter
from pathlib import Path


def compilateur():
    """Fonction d'activation de la compilation"""
    pdflatex(Path(E.get()))


window = tkinter.Tk()
E = tkinter.Entry(window)
f = ""
B = tkinter.Button(window, text="Hello", command=compilateur, default="disabled")
E.pack()
B.pack()
window.mainloop()
