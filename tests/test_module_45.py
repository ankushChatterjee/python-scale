"""Tests for test module 45 — covers src modules [177, 178, 179, 180]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_177 import add_177
from module_178 import subtract_178
from module_179 import multiply_179
from module_180 import divide_180

def test_add_177():
    assert add_177(2, 3) == 5

def test_subtract_178():
    assert subtract_178(10, 4) == 6

def test_multiply_179():
    assert multiply_179(3, 7) == 21

def test_divide_180():
    assert divide_180(10, 2) == 5.0
