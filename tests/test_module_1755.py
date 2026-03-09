"""Tests for test module 1755 — covers src modules [7017, 7018, 7019, 7020]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7017 import add_7017
from module_7018 import subtract_7018
from module_7019 import multiply_7019
from module_7020 import divide_7020

def test_add_7017():
    assert add_7017(2, 3) == 5

def test_subtract_7018():
    assert subtract_7018(10, 4) == 6

def test_multiply_7019():
    assert multiply_7019(3, 7) == 21

def test_divide_7020():
    assert divide_7020(10, 2) == 5.0
