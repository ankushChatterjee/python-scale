"""Tests for test module 1423 — covers src modules [5689, 5690, 5691, 5692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5689 import add_5689
from module_5690 import subtract_5690
from module_5691 import multiply_5691
from module_5692 import divide_5692

def test_add_5689():
    assert add_5689(2, 3) == 5

def test_subtract_5690():
    assert subtract_5690(10, 4) == 6

def test_multiply_5691():
    assert multiply_5691(3, 7) == 21

def test_divide_5692():
    assert divide_5692(10, 2) == 5.0
