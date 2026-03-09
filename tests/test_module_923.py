"""Tests for test module 923 — covers src modules [3689, 3690, 3691, 3692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3689 import add_3689
from module_3690 import subtract_3690
from module_3691 import multiply_3691
from module_3692 import divide_3692

def test_add_3689():
    assert add_3689(2, 3) == 5

def test_subtract_3690():
    assert subtract_3690(10, 4) == 6

def test_multiply_3691():
    assert multiply_3691(3, 7) == 21

def test_divide_3692():
    assert divide_3692(10, 2) == 5.0
