import calc
import unittest

def test_add():
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 2) == 1
    assert calc.add(1, 3) == 4
