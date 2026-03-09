"""Tests for test module 1129 — covers src modules [4513, 4514, 4515, 4516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4513 import add_4513
from module_4514 import subtract_4514
from module_4515 import multiply_4515
from module_4516 import divide_4516

def test_add_4513():
    assert add_4513(2, 3) == 5

def test_subtract_4514():
    assert subtract_4514(10, 4) == 6

def test_multiply_4515():
    assert multiply_4515(3, 7) == 21

def test_divide_4516():
    assert divide_4516(10, 2) == 5.0
