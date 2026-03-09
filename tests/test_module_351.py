"""Tests for test module 351 — covers src modules [1401, 1402, 1403, 1404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1401 import add_1401
from module_1402 import subtract_1402
from module_1403 import multiply_1403
from module_1404 import divide_1404

def test_add_1401():
    assert add_1401(2, 3) == 5

def test_subtract_1402():
    assert subtract_1402(10, 4) == 6

def test_multiply_1403():
    assert multiply_1403(3, 7) == 21

def test_divide_1404():
    assert divide_1404(10, 2) == 5.0
