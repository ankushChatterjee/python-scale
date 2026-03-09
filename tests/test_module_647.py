"""Tests for test module 647 — covers src modules [2585, 2586, 2587, 2588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2585 import add_2585
from module_2586 import subtract_2586
from module_2587 import multiply_2587
from module_2588 import divide_2588

def test_add_2585():
    assert add_2585(2, 3) == 5

def test_subtract_2586():
    assert subtract_2586(10, 4) == 6

def test_multiply_2587():
    assert multiply_2587(3, 7) == 21

def test_divide_2588():
    assert divide_2588(10, 2) == 5.0
