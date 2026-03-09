"""Tests for test module 895 — covers src modules [3577, 3578, 3579, 3580]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3577 import add_3577
from module_3578 import subtract_3578
from module_3579 import multiply_3579
from module_3580 import divide_3580

def test_add_3577():
    assert add_3577(2, 3) == 5

def test_subtract_3578():
    assert subtract_3578(10, 4) == 6

def test_multiply_3579():
    assert multiply_3579(3, 7) == 21

def test_divide_3580():
    assert divide_3580(10, 2) == 5.0
