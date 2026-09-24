import os

ROOT = os.path.dirname(os.path.dirname(__file__))
DESCRIPTION = os.path.join(ROOT, "var", "buffer.txt")


def clear_buffer():
    with open(DESCRIPTION, "w+") as cf:
        cf.write("")


def save_in_buffer(data):
    with open(DESCRIPTION, "a+", encoding="utf-8") as rf:
        rf.write(data + "\n")


