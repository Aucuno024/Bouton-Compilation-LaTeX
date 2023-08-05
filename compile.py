import os


def pdflatex(file: str, delaux: bool):
    """
    :param file: the path to the file
    :param delaux: whether to delete auxiliary files
    :return bool: the Boolean corresponding to the successful compilation of the file
    """
    try:
        f = open(file)
        f.close()
        os.system("pdflatex -aux-directory=auxfile " + file)
        if delaux:
            os.system("echo O | del auxfile")
        return True
    except FileNotFoundError:
        print("not a file")
        return False
