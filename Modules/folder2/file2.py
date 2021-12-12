#!/usr/bin/env python3
import sys, os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../Modules/")
    ),
)

from folder1.file1 import greetings


def my_conversation():
    greetings()
    print("Hello machine")