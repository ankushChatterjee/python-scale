"""Tests for test module 135 — covers src modules [537, 538, 539, 540]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_537 import add_537
from module_538 import subtract_538
from module_539 import multiply_539
from module_540 import divide_540

def test_add_537():
    assert add_537(2, 3) == 5

def test_subtract_538():
    assert subtract_538(10, 4) == 6

def test_multiply_539():
    assert multiply_539(3, 7) == 21

def test_divide_540():
    assert divide_540(10, 2) == 5.0
