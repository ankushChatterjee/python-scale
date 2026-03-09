"""Tests for test module 601 — covers src modules [2401, 2402, 2403, 2404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2401 import add_2401
from module_2402 import subtract_2402
from module_2403 import multiply_2403
from module_2404 import divide_2404

def test_add_2401():
    assert add_2401(2, 3) == 5

def test_subtract_2402():
    assert subtract_2402(10, 4) == 6

def test_multiply_2403():
    assert multiply_2403(3, 7) == 21

def test_divide_2404():
    assert divide_2404(10, 2) == 5.0
