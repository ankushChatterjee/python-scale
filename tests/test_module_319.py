"""Tests for test module 319 — covers src modules [1273, 1274, 1275, 1276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1273 import add_1273
from module_1274 import subtract_1274
from module_1275 import multiply_1275
from module_1276 import divide_1276

def test_add_1273():
    assert add_1273(2, 3) == 5

def test_subtract_1274():
    assert subtract_1274(10, 4) == 6

def test_multiply_1275():
    assert multiply_1275(3, 7) == 21

def test_divide_1276():
    assert divide_1276(10, 2) == 5.0
