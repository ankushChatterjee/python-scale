"""Tests for test module 1343 — covers src modules [5369, 5370, 5371, 5372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5369 import add_5369
from module_5370 import subtract_5370
from module_5371 import multiply_5371
from module_5372 import divide_5372

def test_add_5369():
    assert add_5369(2, 3) == 5

def test_subtract_5370():
    assert subtract_5370(10, 4) == 6

def test_multiply_5371():
    assert multiply_5371(3, 7) == 21

def test_divide_5372():
    assert divide_5372(10, 2) == 5.0
