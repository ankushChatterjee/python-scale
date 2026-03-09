"""Tests for test module 1505 — covers src modules [6017, 6018, 6019, 6020]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6017 import add_6017
from module_6018 import subtract_6018
from module_6019 import multiply_6019
from module_6020 import divide_6020

def test_add_6017():
    assert add_6017(2, 3) == 5

def test_subtract_6018():
    assert subtract_6018(10, 4) == 6

def test_multiply_6019():
    assert multiply_6019(3, 7) == 21

def test_divide_6020():
    assert divide_6020(10, 2) == 5.0
