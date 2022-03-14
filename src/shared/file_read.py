import os
from typing import *


def traverse(path):
    with open(path, "r") as a_file:
        for line in a_file:
            yield line


def read_file(file: str):
    max_lines = 10
    count = 0
    lines = ""
    for line in traverse(file):
        lines += line
        count += 1
        if count >= max_lines:
            return lines
