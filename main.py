from compile import pdflatex
import tkinter
import threading
from os import stat
from time import localtime, asctime
from view import view


def viewer():
    file = E.get()
    thread = threading.Thread(target=view, args=[file])
    thread.start()


def compiler():
    """Calls up the compilation function for the parameters selected in the window."""
    if len(E.get()) > 0:  # if entry is not an empty space
        if len(L.curselection()) == 0:  # check the setting for aux-files
            pdflatex(E.get(), False)
        elif L.curselection()[0] == 0:
            pdflatex(E.get(), True)
        else:
            pdflatex(E.get(), False)


def auto_compiler():
    """Auto calls up the compilation function for the parameters selected in the window."""
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
    """enable or disable the auto compile thread"""
    f = open("auto.txt", "r")
    if len(f.read()) > 2:
        print("on")
        f.close()
        f = open("auto.txt", "w")
        f.write("on")
        f.close()
        thread = threading.Thread(target=auto_compiler)
        thread.start()
    else:
        print("off")
        f.close()
        f = open("auto.txt", "w")
        f.write("off")
        f.close()


window = tkinter.Tk()
window.title("pdfLaTeX compiler")
window.minsize(450, 250)
S = tkinter.Scrollbar(window, orient=tkinter.HORIZONTAL)
E = tkinter.Entry(window, name="path")
B = tkinter.Button(window, text="Compile", command=compiler, default="disabled")
current_var = tkinter.StringVar()
BF = tkinter.Button(window, text="View", command=viewer, default="disabled")
L = tkinter.Listbox(window, height=2, width=25)
L.insert(1, "del aux-files.")
L.insert(2, "keep aux-files.")
L.pack()
BA = tkinter.Button(window, text="Auto compile", command=thread_up, default="disabled")
E.pack()
S.pack(fill=tkinter.X, padx=170)
B.pack()
BA.pack()
BF.pack()
S.config(command=E.xview)
window.mainloop()
