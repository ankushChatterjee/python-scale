"""Tests for test module 2093 — covers src modules [8369, 8370, 8371, 8372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8369 import add_8369
from module_8370 import subtract_8370
from module_8371 import multiply_8371
from module_8372 import divide_8372

def test_add_8369():
    assert add_8369(2, 3) == 5

def test_subtract_8370():
    assert subtract_8370(10, 4) == 6

def test_multiply_8371():
    assert multiply_8371(3, 7) == 21

def test_divide_8372():
    assert divide_8372(10, 2) == 5.0
