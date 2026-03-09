"""Tests for test module 1351 — covers src modules [5401, 5402, 5403, 5404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5401 import add_5401
from module_5402 import subtract_5402
from module_5403 import multiply_5403
from module_5404 import divide_5404

def test_add_5401():
    assert add_5401(2, 3) == 5

def test_subtract_5402():
    assert subtract_5402(10, 4) == 6

def test_multiply_5403():
    assert multiply_5403(3, 7) == 21

def test_divide_5404():
    assert divide_5404(10, 2) == 5.0
