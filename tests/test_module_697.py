"""Tests for test module 697 — covers src modules [2785, 2786, 2787, 2788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2785 import add_2785
from module_2786 import subtract_2786
from module_2787 import multiply_2787
from module_2788 import divide_2788

def test_add_2785():
    assert add_2785(2, 3) == 5

def test_subtract_2786():
    assert subtract_2786(10, 4) == 6

def test_multiply_2787():
    assert multiply_2787(3, 7) == 21

def test_divide_2788():
    assert divide_2788(10, 2) == 5.0
