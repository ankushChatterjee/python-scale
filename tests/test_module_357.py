"""Tests for test module 357 — covers src modules [1425, 1426, 1427, 1428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1425 import add_1425
from module_1426 import subtract_1426
from module_1427 import multiply_1427
from module_1428 import divide_1428

def test_add_1425():
    assert add_1425(2, 3) == 5

def test_subtract_1426():
    assert subtract_1426(10, 4) == 6

def test_multiply_1427():
    assert multiply_1427(3, 7) == 21

def test_divide_1428():
    assert divide_1428(10, 2) == 5.0
