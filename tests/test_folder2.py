#!/usr/bin/env python3
import sys, os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../Modules/")
    ),
)

import test

def test_main(capsys):
    result = test.main()
    captured = capsys.readouterr()
    assert captured.out == ''
