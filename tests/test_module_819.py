"""Tests for test module 819 — covers src modules [3273, 3274, 3275, 3276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3273 import add_3273
from module_3274 import subtract_3274
from module_3275 import multiply_3275
from module_3276 import divide_3276

def test_add_3273():
    assert add_3273(2, 3) == 5

def test_subtract_3274():
    assert subtract_3274(10, 4) == 6

def test_multiply_3275():
    assert multiply_3275(3, 7) == 21

def test_divide_3276():
    assert divide_3276(10, 2) == 5.0
