"""
十大计数
2020-12-06:
"""
from sort import validatetool


def sort1(data):


def sort2(data):


def sort3(data):


def sort4(data):


def sort5(data):


def sort6(data):


def sort7(data):


def sort8(data):


def sort9(data):


def sort10(data):


if __name__ == '__main__':
    local_copy = locals().copy()
    for name, func in local_copy.items():
        if callable(func) and name.startswith('sort'):
            validatetool.validate(func)
