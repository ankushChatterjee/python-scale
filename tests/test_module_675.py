"""Tests for test module 675 — covers src modules [2697, 2698, 2699, 2700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2697 import add_2697
from module_2698 import subtract_2698
from module_2699 import multiply_2699
from module_2700 import divide_2700

def test_add_2697():
    assert add_2697(2, 3) == 5

def test_subtract_2698():
    assert subtract_2698(10, 4) == 6

def test_multiply_2699():
    assert multiply_2699(3, 7) == 21

def test_divide_2700():
    assert divide_2700(10, 2) == 5.0
