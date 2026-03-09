"""Tests for test module 1593 — covers src modules [6369, 6370, 6371, 6372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6369 import add_6369
from module_6370 import subtract_6370
from module_6371 import multiply_6371
from module_6372 import divide_6372

def test_add_6369():
    assert add_6369(2, 3) == 5

def test_subtract_6370():
    assert subtract_6370(10, 4) == 6

def test_multiply_6371():
    assert multiply_6371(3, 7) == 21

def test_divide_6372():
    assert divide_6372(10, 2) == 5.0
