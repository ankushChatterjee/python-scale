"""Tests for test module 1807 — covers src modules [7225, 7226, 7227, 7228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7225 import add_7225
from module_7226 import subtract_7226
from module_7227 import multiply_7227
from module_7228 import divide_7228

def test_add_7225():
    assert add_7225(2, 3) == 5

def test_subtract_7226():
    assert subtract_7226(10, 4) == 6

def test_multiply_7227():
    assert multiply_7227(3, 7) == 21

def test_divide_7228():
    assert divide_7228(10, 2) == 5.0
