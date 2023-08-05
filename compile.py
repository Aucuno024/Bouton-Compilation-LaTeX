import os


def pdflatex(file: str, delaux: bool):
    """
    :param file: le chemin vers le fichier
    :param delaux: suppression ou non des fichiers auxiliaires ?
    :return bool: le booléen correspondant à la réussite de la compilation du fichier
    """
    try:
        os.system("pdflatex -aux-directory=auxfile " + file)
        if delaux:
            os.system("echo O | del auxfile")
        return True
    except BaseException:
        print("error")
        return False
