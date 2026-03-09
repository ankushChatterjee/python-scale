"""Tests for test module 2281 — covers src modules [9121, 9122, 9123, 9124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9121 import add_9121
from module_9122 import subtract_9122
from module_9123 import multiply_9123
from module_9124 import divide_9124

def test_add_9121():
    assert add_9121(2, 3) == 5

def test_subtract_9122():
    assert subtract_9122(10, 4) == 6

def test_multiply_9123():
    assert multiply_9123(3, 7) == 21

def test_divide_9124():
    assert divide_9124(10, 2) == 5.0
