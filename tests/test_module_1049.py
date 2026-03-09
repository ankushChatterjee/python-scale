"""Tests for test module 1049 — covers src modules [4193, 4194, 4195, 4196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4193 import add_4193
from module_4194 import subtract_4194
from module_4195 import multiply_4195
from module_4196 import divide_4196

def test_add_4193():
    assert add_4193(2, 3) == 5

def test_subtract_4194():
    assert subtract_4194(10, 4) == 6

def test_multiply_4195():
    assert multiply_4195(3, 7) == 21

def test_divide_4196():
    assert divide_4196(10, 2) == 5.0
