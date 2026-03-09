"""Tests for test module 2423 — covers src modules [9689, 9690, 9691, 9692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9689 import add_9689
from module_9690 import subtract_9690
from module_9691 import multiply_9691
from module_9692 import divide_9692

def test_add_9689():
    assert add_9689(2, 3) == 5

def test_subtract_9690():
    assert subtract_9690(10, 4) == 6

def test_multiply_9691():
    assert multiply_9691(3, 7) == 21

def test_divide_9692():
    assert divide_9692(10, 2) == 5.0
