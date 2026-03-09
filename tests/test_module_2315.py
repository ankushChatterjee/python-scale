"""Tests for test module 2315 — covers src modules [9257, 9258, 9259, 9260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9257 import add_9257
from module_9258 import subtract_9258
from module_9259 import multiply_9259
from module_9260 import divide_9260

def test_add_9257():
    assert add_9257(2, 3) == 5

def test_subtract_9258():
    assert subtract_9258(10, 4) == 6

def test_multiply_9259():
    assert multiply_9259(3, 7) == 21

def test_divide_9260():
    assert divide_9260(10, 2) == 5.0
