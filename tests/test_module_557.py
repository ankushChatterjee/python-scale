"""Tests for test module 557 — covers src modules [2225, 2226, 2227, 2228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2225 import add_2225
from module_2226 import subtract_2226
from module_2227 import multiply_2227
from module_2228 import divide_2228

def test_add_2225():
    assert add_2225(2, 3) == 5

def test_subtract_2226():
    assert subtract_2226(10, 4) == 6

def test_multiply_2227():
    assert multiply_2227(3, 7) == 21

def test_divide_2228():
    assert divide_2228(10, 2) == 5.0
