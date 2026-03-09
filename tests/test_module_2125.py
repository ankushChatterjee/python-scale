"""Tests for test module 2125 — covers src modules [8497, 8498, 8499, 8500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8497 import add_8497
from module_8498 import subtract_8498
from module_8499 import multiply_8499
from module_8500 import divide_8500

def test_add_8497():
    assert add_8497(2, 3) == 5

def test_subtract_8498():
    assert subtract_8498(10, 4) == 6

def test_multiply_8499():
    assert multiply_8499(3, 7) == 21

def test_divide_8500():
    assert divide_8500(10, 2) == 5.0
