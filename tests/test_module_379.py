"""Tests for test module 379 — covers src modules [1513, 1514, 1515, 1516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1513 import add_1513
from module_1514 import subtract_1514
from module_1515 import multiply_1515
from module_1516 import divide_1516

def test_add_1513():
    assert add_1513(2, 3) == 5

def test_subtract_1514():
    assert subtract_1514(10, 4) == 6

def test_multiply_1515():
    assert multiply_1515(3, 7) == 21

def test_divide_1516():
    assert divide_1516(10, 2) == 5.0
