"""Tests for test module 629 — covers src modules [2513, 2514, 2515, 2516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2513 import add_2513
from module_2514 import subtract_2514
from module_2515 import multiply_2515
from module_2516 import divide_2516

def test_add_2513():
    assert add_2513(2, 3) == 5

def test_subtract_2514():
    assert subtract_2514(10, 4) == 6

def test_multiply_2515():
    assert multiply_2515(3, 7) == 21

def test_divide_2516():
    assert divide_2516(10, 2) == 5.0
