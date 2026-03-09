"""Tests for test module 1569 — covers src modules [6273, 6274, 6275, 6276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6273 import add_6273
from module_6274 import subtract_6274
from module_6275 import multiply_6275
from module_6276 import divide_6276

def test_add_6273():
    assert add_6273(2, 3) == 5

def test_subtract_6274():
    assert subtract_6274(10, 4) == 6

def test_multiply_6275():
    assert multiply_6275(3, 7) == 21

def test_divide_6276():
    assert divide_6276(10, 2) == 5.0
