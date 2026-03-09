"""Tests for test module 1649 — covers src modules [6593, 6594, 6595, 6596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6593 import add_6593
from module_6594 import subtract_6594
from module_6595 import multiply_6595
from module_6596 import divide_6596

def test_add_6593():
    assert add_6593(2, 3) == 5

def test_subtract_6594():
    assert subtract_6594(10, 4) == 6

def test_multiply_6595():
    assert multiply_6595(3, 7) == 21

def test_divide_6596():
    assert divide_6596(10, 2) == 5.0
