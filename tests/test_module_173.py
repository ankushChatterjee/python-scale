"""Tests for test module 173 — covers src modules [689, 690, 691, 692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_689 import add_689
from module_690 import subtract_690
from module_691 import multiply_691
from module_692 import divide_692

def test_add_689():
    assert add_689(2, 3) == 5

def test_subtract_690():
    assert subtract_690(10, 4) == 6

def test_multiply_691():
    assert multiply_691(3, 7) == 21

def test_divide_692():
    assert divide_692(10, 2) == 5.0
