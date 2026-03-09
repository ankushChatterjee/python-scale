"""Tests for test module 2005 — covers src modules [8017, 8018, 8019, 8020]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8017 import add_8017
from module_8018 import subtract_8018
from module_8019 import multiply_8019
from module_8020 import divide_8020

def test_add_8017():
    assert add_8017(2, 3) == 5

def test_subtract_8018():
    assert subtract_8018(10, 4) == 6

def test_multiply_8019():
    assert multiply_8019(3, 7) == 21

def test_divide_8020():
    assert divide_8020(10, 2) == 5.0
