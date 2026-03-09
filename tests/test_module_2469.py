"""Tests for test module 2469 — covers src modules [9873, 9874, 9875, 9876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9873 import add_9873
from module_9874 import subtract_9874
from module_9875 import multiply_9875
from module_9876 import divide_9876

def test_add_9873():
    assert add_9873(2, 3) == 5

def test_subtract_9874():
    assert subtract_9874(10, 4) == 6

def test_multiply_9875():
    assert multiply_9875(3, 7) == 21

def test_divide_9876():
    assert divide_9876(10, 2) == 5.0
