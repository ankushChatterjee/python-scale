"""Tests for test module 255 — covers src modules [1017, 1018, 1019, 1020]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1017 import add_1017
from module_1018 import subtract_1018
from module_1019 import multiply_1019
from module_1020 import divide_1020

def test_add_1017():
    assert add_1017(2, 3) == 5

def test_subtract_1018():
    assert subtract_1018(10, 4) == 6

def test_multiply_1019():
    assert multiply_1019(3, 7) == 21

def test_divide_1020():
    assert divide_1020(10, 2) == 5.0
