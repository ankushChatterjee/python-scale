"""Tests for test module 1101 — covers src modules [4401, 4402, 4403, 4404]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4401 import add_4401
from module_4402 import subtract_4402
from module_4403 import multiply_4403
from module_4404 import divide_4404

def test_add_4401():
    assert add_4401(2, 3) == 5

def test_subtract_4402():
    assert subtract_4402(10, 4) == 6

def test_multiply_4403():
    assert multiply_4403(3, 7) == 21

def test_divide_4404():
    assert divide_4404(10, 2) == 5.0
