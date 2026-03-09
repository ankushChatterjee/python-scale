"""Tests for test module 139 — covers src modules [553, 554, 555, 556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_553 import add_553
from module_554 import subtract_554
from module_555 import multiply_555
from module_556 import divide_556

def test_add_553():
    assert add_553(2, 3) == 5

def test_subtract_554():
    assert subtract_554(10, 4) == 6

def test_multiply_555():
    assert multiply_555(3, 7) == 21

def test_divide_556():
    assert divide_556(10, 2) == 5.0
