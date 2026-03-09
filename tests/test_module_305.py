"""Tests for test module 305 — covers src modules [1217, 1218, 1219, 1220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1217 import add_1217
from module_1218 import subtract_1218
from module_1219 import multiply_1219
from module_1220 import divide_1220

def test_add_1217():
    assert add_1217(2, 3) == 5

def test_subtract_1218():
    assert subtract_1218(10, 4) == 6

def test_multiply_1219():
    assert multiply_1219(3, 7) == 21

def test_divide_1220():
    assert divide_1220(10, 2) == 5.0
