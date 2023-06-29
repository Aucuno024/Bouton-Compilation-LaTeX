import os


def pdflatex(file: str):
    """

    :param file: le chemin vers le fichier
    :return bool: le booléen correspondant à la réussite de la compilation du fichier
    """
    try:
        os.system("pdflatex -aux-directory=auxfile " + file)
        os.system("echo O | del auxfile")
        return True
    except BaseException:
        print("f")
        return False
