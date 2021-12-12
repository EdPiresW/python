#!/usr/bin/env python3
from Modules.folder1.file1 import greetings
from Modules.folder2 import my_conversation

def main():
    print("Passo 1")
    greetings()
    print("Passo 2")
    my_conversation()

if __name__ == '__main__':
    main()