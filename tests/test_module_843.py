"""Tests for test module 843 — covers src modules [3369, 3370, 3371, 3372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3369 import add_3369
from module_3370 import subtract_3370
from module_3371 import multiply_3371
from module_3372 import divide_3372

def test_add_3369():
    assert add_3369(2, 3) == 5

def test_subtract_3370():
    assert subtract_3370(10, 4) == 6

def test_multiply_3371():
    assert multiply_3371(3, 7) == 21

def test_divide_3372():
    assert divide_3372(10, 2) == 5.0
