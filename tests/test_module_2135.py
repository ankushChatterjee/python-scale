"""Tests for test module 2135 — covers src modules [8537, 8538, 8539, 8540]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8537 import add_8537
from module_8538 import subtract_8538
from module_8539 import multiply_8539
from module_8540 import divide_8540

def test_add_8537():
    assert add_8537(2, 3) == 5

def test_subtract_8538():
    assert subtract_8538(10, 4) == 6

def test_multiply_8539():
    assert multiply_8539(3, 7) == 21

def test_divide_8540():
    assert divide_8540(10, 2) == 5.0
