"""Tests for test module 1665 — covers src modules [6657, 6658, 6659, 6660]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6657 import add_6657
from module_6658 import subtract_6658
from module_6659 import multiply_6659
from module_6660 import divide_6660

def test_add_6657():
    assert add_6657(2, 3) == 5

def test_subtract_6658():
    assert subtract_6658(10, 4) == 6

def test_multiply_6659():
    assert multiply_6659(3, 7) == 21

def test_divide_6660():
    assert divide_6660(10, 2) == 5.0
