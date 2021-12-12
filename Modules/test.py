#!/usr/bin/env python3
from folder1 import greetings, get_name
from folder2 import my_conversation


def main():
    if get_name() == "Edgar_01":
        print("Passo 1")
        greetings()
        print("Passo 2")
        my_conversation()


if __name__ == '__main__':
    main()