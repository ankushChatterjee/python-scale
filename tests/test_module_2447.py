"""Tests for test module 2447 — covers src modules [9785, 9786, 9787, 9788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9785 import add_9785
from module_9786 import subtract_9786
from module_9787 import multiply_9787
from module_9788 import divide_9788

def test_add_9785():
    assert add_9785(2, 3) == 5

def test_subtract_9786():
    assert subtract_9786(10, 4) == 6

def test_multiply_9787():
    assert multiply_9787(3, 7) == 21

def test_divide_9788():
    assert divide_9788(10, 2) == 5.0
