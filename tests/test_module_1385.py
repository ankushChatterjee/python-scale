"""Tests for test module 1385 — covers src modules [5537, 5538, 5539, 5540]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5537 import add_5537
from module_5538 import subtract_5538
from module_5539 import multiply_5539
from module_5540 import divide_5540

def test_add_5537():
    assert add_5537(2, 3) == 5

def test_subtract_5538():
    assert subtract_5538(10, 4) == 6

def test_multiply_5539():
    assert multiply_5539(3, 7) == 21

def test_divide_5540():
    assert divide_5540(10, 2) == 5.0
