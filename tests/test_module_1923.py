"""Tests for test module 1923 — covers src modules [7689, 7690, 7691, 7692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7689 import add_7689
from module_7690 import subtract_7690
from module_7691 import multiply_7691
from module_7692 import divide_7692

def test_add_7689():
    assert add_7689(2, 3) == 5

def test_subtract_7690():
    assert subtract_7690(10, 4) == 6

def test_multiply_7691():
    assert multiply_7691(3, 7) == 21

def test_divide_7692():
    assert divide_7692(10, 2) == 5.0
