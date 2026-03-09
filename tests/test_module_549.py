"""Tests for test module 549 — covers src modules [2193, 2194, 2195, 2196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2193 import add_2193
from module_2194 import subtract_2194
from module_2195 import multiply_2195
from module_2196 import divide_2196

def test_add_2193():
    assert add_2193(2, 3) == 5

def test_subtract_2194():
    assert subtract_2194(10, 4) == 6

def test_multiply_2195():
    assert multiply_2195(3, 7) == 21

def test_divide_2196():
    assert divide_2196(10, 2) == 5.0
