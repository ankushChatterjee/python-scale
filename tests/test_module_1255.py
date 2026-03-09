"""Tests for test module 1255 — covers src modules [5017, 5018, 5019, 5020]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5017 import add_5017
from module_5018 import subtract_5018
from module_5019 import multiply_5019
from module_5020 import divide_5020

def test_add_5017():
    assert add_5017(2, 3) == 5

def test_subtract_5018():
    assert subtract_5018(10, 4) == 6

def test_multiply_5019():
    assert multiply_5019(3, 7) == 21

def test_divide_5020():
    assert divide_5020(10, 2) == 5.0
