"""Tests for test module 1299 — covers src modules [5193, 5194, 5195, 5196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5193 import add_5193
from module_5194 import subtract_5194
from module_5195 import multiply_5195
from module_5196 import divide_5196

def test_add_5193():
    assert add_5193(2, 3) == 5

def test_subtract_5194():
    assert subtract_5194(10, 4) == 6

def test_multiply_5195():
    assert multiply_5195(3, 7) == 21

def test_divide_5196():
    assert divide_5196(10, 2) == 5.0
