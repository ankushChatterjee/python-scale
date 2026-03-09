"""Tests for test module 1555 — covers src modules [6217, 6218, 6219, 6220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6217 import add_6217
from module_6218 import subtract_6218
from module_6219 import multiply_6219
from module_6220 import divide_6220

def test_add_6217():
    assert add_6217(2, 3) == 5

def test_subtract_6218():
    assert subtract_6218(10, 4) == 6

def test_multiply_6219():
    assert multiply_6219(3, 7) == 21

def test_divide_6220():
    assert divide_6220(10, 2) == 5.0
