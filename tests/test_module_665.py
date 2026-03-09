"""Tests for test module 665 — covers src modules [2657, 2658, 2659, 2660]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2657 import add_2657
from module_2658 import subtract_2658
from module_2659 import multiply_2659
from module_2660 import divide_2660

def test_add_2657():
    assert add_2657(2, 3) == 5

def test_subtract_2658():
    assert subtract_2658(10, 4) == 6

def test_multiply_2659():
    assert multiply_2659(3, 7) == 21

def test_divide_2660():
    assert divide_2660(10, 2) == 5.0
