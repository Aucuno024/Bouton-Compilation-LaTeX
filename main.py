from compile import pdflatex
import tkinter



def compilateur():
    """Fonction d'activation de la compilation"""
    if len(E.get()) > 0:
        if len(L.curselection()) == 0:
            pdflatex(E.get(), False)
        elif L.curselection()[0] == 0:
            pdflatex(E.get(), True)
        else:
            pdflatex(E.get(), False)


window = tkinter.Tk()
E = tkinter.Entry(window)
B = tkinter.Button(window, text="Compile", command=compilateur, default="disabled")
current_var = tkinter.StringVar()
L = tkinter.Listbox(window, height=2, width=25)
L.insert(1, "Supprimer fichiers auxliaires.")
L.insert(2, "Laisser fichiers auxiliaires.")
L.pack()
E.pack()
B.pack()
window.mainloop()
