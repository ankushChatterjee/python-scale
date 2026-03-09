"""Tests for test module 2319 — covers src modules [9273, 9274, 9275, 9276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9273 import add_9273
from module_9274 import subtract_9274
from module_9275 import multiply_9275
from module_9276 import divide_9276

def test_add_9273():
    assert add_9273(2, 3) == 5

def test_subtract_9274():
    assert subtract_9274(10, 4) == 6

def test_multiply_9275():
    assert multiply_9275(3, 7) == 21

def test_divide_9276():
    assert divide_9276(10, 2) == 5.0
