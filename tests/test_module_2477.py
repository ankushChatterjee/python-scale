"""Tests for test module 2477 — covers src modules [9905, 9906, 9907, 9908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9905 import add_9905
from module_9906 import subtract_9906
from module_9907 import multiply_9907
from module_9908 import divide_9908

def test_add_9905():
    assert add_9905(2, 3) == 5

def test_subtract_9906():
    assert subtract_9906(10, 4) == 6

def test_multiply_9907():
    assert multiply_9907(3, 7) == 21

def test_divide_9908():
    assert divide_9908(10, 2) == 5.0
