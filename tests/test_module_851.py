"""Tests for test module 851 — covers src modules [3401, 3402, 3403, 3404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3401 import add_3401
from module_3402 import subtract_3402
from module_3403 import multiply_3403
from module_3404 import divide_3404

def test_add_3401():
    assert add_3401(2, 3) == 5

def test_subtract_3402():
    assert subtract_3402(10, 4) == 6

def test_multiply_3403():
    assert multiply_3403(3, 7) == 21

def test_divide_3404():
    assert divide_3404(10, 2) == 5.0
