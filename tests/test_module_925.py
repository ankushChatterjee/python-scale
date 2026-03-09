"""Tests for test module 925 — covers src modules [3697, 3698, 3699, 3700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3697 import add_3697
from module_3698 import subtract_3698
from module_3699 import multiply_3699
from module_3700 import divide_3700

def test_add_3697():
    assert add_3697(2, 3) == 5

def test_subtract_3698():
    assert subtract_3698(10, 4) == 6

def test_multiply_3699():
    assert multiply_3699(3, 7) == 21

def test_divide_3700():
    assert divide_3700(10, 2) == 5.0
