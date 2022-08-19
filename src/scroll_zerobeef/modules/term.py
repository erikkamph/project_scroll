#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

config = {
    "min_width": 20,
    "preferred_width": 20,
    "preferred_columns": 2
}


def terminal_size():
    # Get the size of the terminal
    data = os.popen("stty size", "r").read()
    return data.split()


def set_preferred(integer, columns=False, width=False):
    if type(integer) not in (int, float, str):
        raise TypeError("integer must be a string or a number")
    if type(integer) is str and re.search(r'\d{1,2}', integer, re.UNICODE) is None:
        raise ValueError("integer must be a string consisting of 1 or 2 characters")
    converted = int(integer)
    config["preferred_columns" if columns else "preferred_width" if width else None] = converted


def test_column_size():
    size = list(map(lambda item: int(item), terminal_size()))
    nr_preferred_columns = size[1] // config["preferred_width"]
    nr_preferred_width = size[1] // config["preferred_columns"]
    nr_columns = size[1] // config["min_width"]
    return False if nr_preferred_columns > nr_columns or nr_preferred_width < config["min_width"] else True
