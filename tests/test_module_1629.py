"""Tests for test module 1629 — covers src modules [6513, 6514, 6515, 6516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6513 import add_6513
from module_6514 import subtract_6514
from module_6515 import multiply_6515
from module_6516 import divide_6516

def test_add_6513():
    assert add_6513(2, 3) == 5

def test_subtract_6514():
    assert subtract_6514(10, 4) == 6

def test_multiply_6515():
    assert multiply_6515(3, 7) == 21

def test_divide_6516():
    assert divide_6516(10, 2) == 5.0
