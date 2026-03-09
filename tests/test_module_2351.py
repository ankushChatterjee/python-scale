"""Tests for test module 2351 — covers src modules [9401, 9402, 9403, 9404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9401 import add_9401
from module_9402 import subtract_9402
from module_9403 import multiply_9403
from module_9404 import divide_9404

def test_add_9401():
    assert add_9401(2, 3) == 5

def test_subtract_9402():
    assert subtract_9402(10, 4) == 6

def test_multiply_9403():
    assert multiply_9403(3, 7) == 21

def test_divide_9404():
    assert divide_9404(10, 2) == 5.0
