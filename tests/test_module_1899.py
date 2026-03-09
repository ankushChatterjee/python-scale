"""Tests for test module 1899 — covers src modules [7593, 7594, 7595, 7596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7593 import add_7593
from module_7594 import subtract_7594
from module_7595 import multiply_7595
from module_7596 import divide_7596

def test_add_7593():
    assert add_7593(2, 3) == 5

def test_subtract_7594():
    assert subtract_7594(10, 4) == 6

def test_multiply_7595():
    assert multiply_7595(3, 7) == 21

def test_divide_7596():
    assert divide_7596(10, 2) == 5.0
