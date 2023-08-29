import os


def view(file: str):
    if len(file) > 0:
        if os.name != "nt":
            print("Linux")
        else:
            try:
                file = file.replace(".tex", ".pdf")
                f = open(file)
                f.close()
                os.system(file)
                return True
            except FileNotFoundError:
                print("not a file")
                return False
