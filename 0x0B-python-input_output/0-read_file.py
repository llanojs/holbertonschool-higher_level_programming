#!/usr/bin/python3
"""In this module it read a File"""


def read_file(filename=""):
    """This  function that reads a text file (UTF8) and"""
    with open("my_file_0.txt", mode='r', encoding="utf-8") as my_file:
        print(my_file.read())
    my_file.close()