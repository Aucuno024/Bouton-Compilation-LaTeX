import os


def pdflatex(file: str):
    try:
        f = open(file)
        f.close()
        os.system("pdflatex -aux-directory=auxfile " + file)
        os.system("del auxfile")
        return True
    except BaseException:
        print("f")
        return False
