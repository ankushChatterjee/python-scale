"""Tests for test module 311 — covers src modules [1241, 1242, 1243, 1244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1241 import add_1241
from module_1242 import subtract_1242
from module_1243 import multiply_1243
from module_1244 import divide_1244

def test_add_1241():
    assert add_1241(2, 3) == 5

def test_subtract_1242():
    assert subtract_1242(10, 4) == 6

def test_multiply_1243():
    assert multiply_1243(3, 7) == 21

def test_divide_1244():
    assert divide_1244(10, 2) == 5.0
