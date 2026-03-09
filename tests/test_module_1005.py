"""Tests for test module 1005 — covers src modules [4017, 4018, 4019, 4020]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4017 import add_4017
from module_4018 import subtract_4018
from module_4019 import multiply_4019
from module_4020 import divide_4020

def test_add_4017():
    assert add_4017(2, 3) == 5

def test_subtract_4018():
    assert subtract_4018(10, 4) == 6

def test_multiply_4019():
    assert multiply_4019(3, 7) == 21

def test_divide_4020():
    assert divide_4020(10, 2) == 5.0
