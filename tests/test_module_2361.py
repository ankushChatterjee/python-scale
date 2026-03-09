"""Tests for test module 2361 — covers src modules [9441, 9442, 9443, 9444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9441 import add_9441
from module_9442 import subtract_9442
from module_9443 import multiply_9443
from module_9444 import divide_9444

def test_add_9441():
    assert add_9441(2, 3) == 5

def test_subtract_9442():
    assert subtract_9442(10, 4) == 6

def test_multiply_9443():
    assert multiply_9443(3, 7) == 21

def test_divide_9444():
    assert divide_9444(10, 2) == 5.0
