"""Tests for test module 385 — covers src modules [1537, 1538, 1539, 1540]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1537 import add_1537
from module_1538 import subtract_1538
from module_1539 import multiply_1539
from module_1540 import divide_1540

def test_add_1537():
    assert add_1537(2, 3) == 5

def test_subtract_1538():
    assert subtract_1538(10, 4) == 6

def test_multiply_1539():
    assert multiply_1539(3, 7) == 21

def test_divide_1540():
    assert divide_1540(10, 2) == 5.0
