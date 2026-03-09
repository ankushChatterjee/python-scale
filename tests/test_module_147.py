"""Tests for test module 147 — covers src modules [585, 586, 587, 588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_585 import add_585
from module_586 import subtract_586
from module_587 import multiply_587
from module_588 import divide_588

def test_add_585():
    assert add_585(2, 3) == 5

def test_subtract_586():
    assert subtract_586(10, 4) == 6

def test_multiply_587():
    assert multiply_587(3, 7) == 21

def test_divide_588():
    assert divide_588(10, 2) == 5.0
