"""Tests for test module 805 — covers src modules [3217, 3218, 3219, 3220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3217 import add_3217
from module_3218 import subtract_3218
from module_3219 import multiply_3219
from module_3220 import divide_3220

def test_add_3217():
    assert add_3217(2, 3) == 5

def test_subtract_3218():
    assert subtract_3218(10, 4) == 6

def test_multiply_3219():
    assert multiply_3219(3, 7) == 21

def test_divide_3220():
    assert divide_3220(10, 2) == 5.0
