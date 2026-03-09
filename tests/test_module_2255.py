"""Tests for test module 2255 — covers src modules [9017, 9018, 9019, 9020]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9017 import add_9017
from module_9018 import subtract_9018
from module_9019 import multiply_9019
from module_9020 import divide_9020

def test_add_9017():
    assert add_9017(2, 3) == 5

def test_subtract_9018():
    assert subtract_9018(10, 4) == 6

def test_multiply_9019():
    assert multiply_9019(3, 7) == 21

def test_divide_9020():
    assert divide_9020(10, 2) == 5.0
