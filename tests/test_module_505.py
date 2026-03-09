"""Tests for test module 505 — covers src modules [2017, 2018, 2019, 2020]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2017 import add_2017
from module_2018 import subtract_2018
from module_2019 import multiply_2019
from module_2020 import divide_2020

def test_add_2017():
    assert add_2017(2, 3) == 5

def test_subtract_2018():
    assert subtract_2018(10, 4) == 6

def test_multiply_2019():
    assert multiply_2019(3, 7) == 21

def test_divide_2020():
    assert divide_2020(10, 2) == 5.0
