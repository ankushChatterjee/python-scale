"""Tests for test module 1379 — covers src modules [5513, 5514, 5515, 5516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5513 import add_5513
from module_5514 import subtract_5514
from module_5515 import multiply_5515
from module_5516 import divide_5516

def test_add_5513():
    assert add_5513(2, 3) == 5

def test_subtract_5514():
    assert subtract_5514(10, 4) == 6

def test_multiply_5515():
    assert multiply_5515(3, 7) == 21

def test_divide_5516():
    assert divide_5516(10, 2) == 5.0
