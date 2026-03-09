"""Tests for test module 1549 — covers src modules [6193, 6194, 6195, 6196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6193 import add_6193
from module_6194 import subtract_6194
from module_6195 import multiply_6195
from module_6196 import divide_6196

def test_add_6193():
    assert add_6193(2, 3) == 5

def test_subtract_6194():
    assert subtract_6194(10, 4) == 6

def test_multiply_6195():
    assert multiply_6195(3, 7) == 21

def test_divide_6196():
    assert divide_6196(10, 2) == 5.0
