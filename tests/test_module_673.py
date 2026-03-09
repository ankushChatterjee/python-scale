"""Tests for test module 673 — covers src modules [2689, 2690, 2691, 2692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2689 import add_2689
from module_2690 import subtract_2690
from module_2691 import multiply_2691
from module_2692 import divide_2692

def test_add_2689():
    assert add_2689(2, 3) == 5

def test_subtract_2690():
    assert subtract_2690(10, 4) == 6

def test_multiply_2691():
    assert multiply_2691(3, 7) == 21

def test_divide_2692():
    assert divide_2692(10, 2) == 5.0
