"""Tests for test module 593 — covers src modules [2369, 2370, 2371, 2372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2369 import add_2369
from module_2370 import subtract_2370
from module_2371 import multiply_2371
from module_2372 import divide_2372

def test_add_2369():
    assert add_2369(2, 3) == 5

def test_subtract_2370():
    assert subtract_2370(10, 4) == 6

def test_multiply_2371():
    assert multiply_2371(3, 7) == 21

def test_divide_2372():
    assert divide_2372(10, 2) == 5.0
