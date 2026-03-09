"""Tests for test module 2411 — covers src modules [9641, 9642, 9643, 9644]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9641 import add_9641
from module_9642 import subtract_9642
from module_9643 import multiply_9643
from module_9644 import divide_9644

def test_add_9641():
    assert add_9641(2, 3) == 5

def test_subtract_9642():
    assert subtract_9642(10, 4) == 6

def test_multiply_9643():
    assert multiply_9643(3, 7) == 21

def test_divide_9644():
    assert divide_9644(10, 2) == 5.0
