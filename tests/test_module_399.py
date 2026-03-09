"""Tests for test module 399 — covers src modules [1593, 1594, 1595, 1596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1593 import add_1593
from module_1594 import subtract_1594
from module_1595 import multiply_1595
from module_1596 import divide_1596

def test_add_1593():
    assert add_1593(2, 3) == 5

def test_subtract_1594():
    assert subtract_1594(10, 4) == 6

def test_multiply_1595():
    assert multiply_1595(3, 7) == 21

def test_divide_1596():
    assert divide_1596(10, 2) == 5.0
