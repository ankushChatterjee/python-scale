"""Tests for test module 2049 — covers src modules [8193, 8194, 8195, 8196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8193 import add_8193
from module_8194 import subtract_8194
from module_8195 import multiply_8195
from module_8196 import divide_8196

def test_add_8193():
    assert add_8193(2, 3) == 5

def test_subtract_8194():
    assert subtract_8194(10, 4) == 6

def test_multiply_8195():
    assert multiply_8195(3, 7) == 21

def test_divide_8196():
    assert divide_8196(10, 2) == 5.0
