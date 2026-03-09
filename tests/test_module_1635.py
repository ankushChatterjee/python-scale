"""Tests for test module 1635 — covers src modules [6537, 6538, 6539, 6540]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6537 import add_6537
from module_6538 import subtract_6538
from module_6539 import multiply_6539
from module_6540 import divide_6540

def test_add_6537():
    assert add_6537(2, 3) == 5

def test_subtract_6538():
    assert subtract_6538(10, 4) == 6

def test_multiply_6539():
    assert multiply_6539(3, 7) == 21

def test_divide_6540():
    assert divide_6540(10, 2) == 5.0
