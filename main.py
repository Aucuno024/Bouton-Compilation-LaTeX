from compile import pdflatex
import tkinter
import threading
from os import stat
from stat import ST_MTIME
from time import localtime, asctime, sleep


def compilateur():
    """Fonction d'activation de la compilation"""
    if len(E.get()) > 0:
        if len(L.curselection()) == 0:
            pdflatex(E.get(), False)
        elif L.curselection()[0] == 0:
            pdflatex(E.get(), True)
        else:
            pdflatex(E.get(), False)


def auto_compilateur():
    while True:
        f = open("auto.txt", "r")
        text = f.read()
        f.close()
        if text != "on":
            break
        if len(E.get()) != 0:
            try:
                f = open(E.get(), "r")
                f.close()
                if asctime(localtime()) == asctime(localtime(stat(E.get())[8])):
                    if len(L.curselection()) == 0:
                        pdflatex(E.get(), False)
                    elif L.curselection()[0] == 0:
                        pdflatex(E.get(), True)
                    else:
                        pdflatex(E.get(), False)
            except FileNotFoundError:
                print("error")


def thread_up():
    f = open("auto.txt", "r")
    if len(f.read()) > 2:
        print("on")
        f.close()
        f = open("auto.txt", "w")
        f.write("on")
        f.close()
        thread = threading.Thread(target=auto_compilateur)
        thread.start()
    else:
        print("off")
        f.close()
        f = open("auto.txt", "w")
        f.write("off")
        f.close()


window = tkinter.Tk()
window.title("PdfLaTeX compilator")
window.minsize(500, 200)
S = tkinter.Scrollbar(window, orient=tkinter.HORIZONTAL)
E = tkinter.Entry(window, name="path", xscrollcommand=S)
B = tkinter.Button(window, text="Compile", command=compilateur, default="disabled")
current_var = tkinter.StringVar()
L = tkinter.Listbox(window, height=2, width=25)
L.insert(1, "del auxfiles.")
L.insert(2, "keep auxfiles.")
L.pack()
BA = tkinter.Button(window, text="Auto compile", command=thread_up, default="disabled")
E.pack()
S.pack(fill=tkinter.X, padx=170)
B.pack()
BA.pack()
S.config(command=E.xview)
window.mainloop()
