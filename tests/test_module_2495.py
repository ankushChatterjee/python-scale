"""Tests for test module 2495 — covers src modules [9977, 9978, 9979, 9980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9977 import add_9977
from module_9978 import subtract_9978
from module_9979 import multiply_9979
from module_9980 import divide_9980

def test_add_9977():
    assert add_9977(2, 3) == 5

def test_subtract_9978():
    assert subtract_9978(10, 4) == 6

def test_multiply_9979():
    assert multiply_9979(3, 7) == 21

def test_divide_9980():
    assert divide_9980(10, 2) == 5.0
