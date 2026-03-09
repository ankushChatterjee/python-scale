"""Tests for test module 755 — covers src modules [3017, 3018, 3019, 3020]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3017 import add_3017
from module_3018 import subtract_3018
from module_3019 import multiply_3019
from module_3020 import divide_3020

def test_add_3017():
    assert add_3017(2, 3) == 5

def test_subtract_3018():
    assert subtract_3018(10, 4) == 6

def test_multiply_3019():
    assert multiply_3019(3, 7) == 21

def test_divide_3020():
    assert divide_3020(10, 2) == 5.0
