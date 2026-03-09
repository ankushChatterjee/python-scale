"""Tests for test module 1799 — covers src modules [7193, 7194, 7195, 7196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7193 import add_7193
from module_7194 import subtract_7194
from module_7195 import multiply_7195
from module_7196 import divide_7196

def test_add_7193():
    assert add_7193(2, 3) == 5

def test_subtract_7194():
    assert subtract_7194(10, 4) == 6

def test_multiply_7195():
    assert multiply_7195(3, 7) == 21

def test_divide_7196():
    assert divide_7196(10, 2) == 5.0
