"""Tests for test module 61 — covers src modules [241, 242, 243, 244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_241 import add_241
from module_242 import subtract_242
from module_243 import multiply_243
from module_244 import divide_244

def test_add_241():
    assert add_241(2, 3) == 5

def test_subtract_242():
    assert subtract_242(10, 4) == 6

def test_multiply_243():
    assert multiply_243(3, 7) == 21

def test_divide_244():
    assert divide_244(10, 2) == 5.0
