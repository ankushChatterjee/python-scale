"""Tests for test module 1173 — covers src modules [4689, 4690, 4691, 4692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4689 import add_4689
from module_4690 import subtract_4690
from module_4691 import multiply_4691
from module_4692 import divide_4692

def test_add_4689():
    assert add_4689(2, 3) == 5

def test_subtract_4690():
    assert subtract_4690(10, 4) == 6

def test_multiply_4691():
    assert multiply_4691(3, 7) == 21

def test_divide_4692():
    assert divide_4692(10, 2) == 5.0
