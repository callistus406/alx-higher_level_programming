#!/usr/bin/python3
"""
This program reads a text file in format UTF-8
"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as fd:
        for line in fd:
            print(line, end="")
