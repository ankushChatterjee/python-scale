"""Tests for test module 2101 — covers src modules [8401, 8402, 8403, 8404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8401 import add_8401
from module_8402 import subtract_8402
from module_8403 import multiply_8403
from module_8404 import divide_8404

def test_add_8401():
    assert add_8401(2, 3) == 5

def test_subtract_8402():
    assert subtract_8402(10, 4) == 6

def test_multiply_8403():
    assert multiply_8403(3, 7) == 21

def test_divide_8404():
    assert divide_8404(10, 2) == 5.0
