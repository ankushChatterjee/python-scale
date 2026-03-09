"""Tests for test module 129 — covers src modules [513, 514, 515, 516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_513 import add_513
from module_514 import subtract_514
from module_515 import multiply_515
from module_516 import divide_516

def test_add_513():
    assert add_513(2, 3) == 5

def test_subtract_514():
    assert subtract_514(10, 4) == 6

def test_multiply_515():
    assert multiply_515(3, 7) == 21

def test_divide_516():
    assert divide_516(10, 2) == 5.0
