"""Tests for test module 1897 — covers src modules [7585, 7586, 7587, 7588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7585 import add_7585
from module_7586 import subtract_7586
from module_7587 import multiply_7587
from module_7588 import divide_7588

def test_add_7585():
    assert add_7585(2, 3) == 5

def test_subtract_7586():
    assert subtract_7586(10, 4) == 6

def test_multiply_7587():
    assert multiply_7587(3, 7) == 21

def test_divide_7588():
    assert divide_7588(10, 2) == 5.0
