import os
from time import localtime, asctime


def pdflatex(file: str, delaux: bool):
    """
    :param file: the path to the file
    :param delaux: whether to delete auxiliary files
    :return bool: the Boolean corresponding to the successful compilation of the file
    """
    try:
        f = open(file)
        f.close()
        f = open("view.txt")
        if f.read() == "on":
            input("Attention vous visionniez jusqu'à présent votre documment, est-ce toujours le cas ? Si oui veuillez "
                  "fermer votre visionneur afin de pouvoir compiler puis pressez entrer.")
        os.system("pdflatex -aux-directory=auxfile " + file)
        if asctime(localtime()) == asctime(localtime(os.stat(file)[8])):
            f.write("off")
        if delaux:
            os.system("echo O | del auxfile")
        return True
    except FileNotFoundError:
        print("not a file")
        return False
