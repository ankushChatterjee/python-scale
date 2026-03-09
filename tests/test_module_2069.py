"""Tests for test module 2069 — covers src modules [8273, 8274, 8275, 8276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8273 import add_8273
from module_8274 import subtract_8274
from module_8275 import multiply_8275
from module_8276 import divide_8276

def test_add_8273():
    assert add_8273(2, 3) == 5

def test_subtract_8274():
    assert subtract_8274(10, 4) == 6

def test_multiply_8275():
    assert multiply_8275(3, 7) == 21

def test_divide_8276():
    assert divide_8276(10, 2) == 5.0
