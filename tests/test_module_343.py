"""Tests for test module 343 — covers src modules [1369, 1370, 1371, 1372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1369 import add_1369
from module_1370 import subtract_1370
from module_1371 import multiply_1371
from module_1372 import divide_1372

def test_add_1369():
    assert add_1369(2, 3) == 5

def test_subtract_1370():
    assert subtract_1370(10, 4) == 6

def test_multiply_1371():
    assert multiply_1371(3, 7) == 21

def test_divide_1372():
    assert divide_1372(10, 2) == 5.0
