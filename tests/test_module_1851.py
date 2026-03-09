"""Tests for test module 1851 — covers src modules [7401, 7402, 7403, 7404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7401 import add_7401
from module_7402 import subtract_7402
from module_7403 import multiply_7403
from module_7404 import divide_7404

def test_add_7401():
    assert add_7401(2, 3) == 5

def test_subtract_7402():
    assert subtract_7402(10, 4) == 6

def test_multiply_7403():
    assert multiply_7403(3, 7) == 21

def test_divide_7404():
    assert divide_7404(10, 2) == 5.0
