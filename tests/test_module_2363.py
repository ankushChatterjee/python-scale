"""Tests for test module 2363 — covers src modules [9449, 9450, 9451, 9452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9449 import add_9449
from module_9450 import subtract_9450
from module_9451 import multiply_9451
from module_9452 import divide_9452

def test_add_9449():
    assert add_9449(2, 3) == 5

def test_subtract_9450():
    assert subtract_9450(10, 4) == 6

def test_multiply_9451():
    assert multiply_9451(3, 7) == 21

def test_divide_9452():
    assert divide_9452(10, 2) == 5.0
