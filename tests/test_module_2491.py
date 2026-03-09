"""Tests for test module 2491 — covers src modules [9961, 9962, 9963, 9964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9961 import add_9961
from module_9962 import subtract_9962
from module_9963 import multiply_9963
from module_9964 import divide_9964

def test_add_9961():
    assert add_9961(2, 3) == 5

def test_subtract_9962():
    assert subtract_9962(10, 4) == 6

def test_multiply_9963():
    assert multiply_9963(3, 7) == 21

def test_divide_9964():
    assert divide_9964(10, 2) == 5.0
