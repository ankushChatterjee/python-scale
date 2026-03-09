"""Tests for test module 101 — covers src modules [401, 402, 403, 404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_401 import add_401
from module_402 import subtract_402
from module_403 import multiply_403
from module_404 import divide_404

def test_add_401():
    assert add_401(2, 3) == 5

def test_subtract_402():
    assert subtract_402(10, 4) == 6

def test_multiply_403():
    assert multiply_403(3, 7) == 21

def test_divide_404():
    assert divide_404(10, 2) == 5.0
