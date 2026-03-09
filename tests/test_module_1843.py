"""Tests for test module 1843 — covers src modules [7369, 7370, 7371, 7372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7369 import add_7369
from module_7370 import subtract_7370
from module_7371 import multiply_7371
from module_7372 import divide_7372

def test_add_7369():
    assert add_7369(2, 3) == 5

def test_subtract_7370():
    assert subtract_7370(10, 4) == 6

def test_multiply_7371():
    assert multiply_7371(3, 7) == 21

def test_divide_7372():
    assert divide_7372(10, 2) == 5.0
