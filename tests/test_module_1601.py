"""Tests for test module 1601 — covers src modules [6401, 6402, 6403, 6404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6401 import add_6401
from module_6402 import subtract_6402
from module_6403 import multiply_6403
from module_6404 import divide_6404

def test_add_6401():
    assert add_6401(2, 3) == 5

def test_subtract_6402():
    assert subtract_6402(10, 4) == 6

def test_multiply_6403():
    assert multiply_6403(3, 7) == 21

def test_divide_6404():
    assert divide_6404(10, 2) == 5.0
