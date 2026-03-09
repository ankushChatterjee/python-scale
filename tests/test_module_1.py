"""Tests for test module 1 — covers src modules [1, 2, 3, 4]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1 import add_1
from module_2 import subtract_2
from module_3 import multiply_3
from module_4 import divide_4

def test_add_1():
    assert add_1(2, 3) == 5

def test_subtract_2():
    assert subtract_2(10, 4) == 6

def test_multiply_3():
    assert multiply_3(3, 7) == 21

def test_divide_4():
    assert divide_4(10, 2) == 5.0
