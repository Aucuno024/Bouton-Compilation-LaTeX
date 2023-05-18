from compile import pdflatex
import tkinter


def compilateur():
    pdflatex(E.get())


window = tkinter.Tk()
E = tkinter.Entry(window)
f = ""
B = tkinter.Button(window, text="Hello", command=compilateur, default="disabled")
E.pack()
B.pack()
window.mainloop()
