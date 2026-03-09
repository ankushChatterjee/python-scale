"""Tests for test module 1305 — covers src modules [5217, 5218, 5219, 5220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5217 import add_5217
from module_5218 import subtract_5218
from module_5219 import multiply_5219
from module_5220 import divide_5220

def test_add_5217():
    assert add_5217(2, 3) == 5

def test_subtract_5218():
    assert subtract_5218(10, 4) == 6

def test_multiply_5219():
    assert multiply_5219(3, 7) == 21

def test_divide_5220():
    assert divide_5220(10, 2) == 5.0
