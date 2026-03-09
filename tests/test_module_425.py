"""Tests for test module 425 — covers src modules [1697, 1698, 1699, 1700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1697 import add_1697
from module_1698 import subtract_1698
from module_1699 import multiply_1699
from module_1700 import divide_1700

def test_add_1697():
    assert add_1697(2, 3) == 5

def test_subtract_1698():
    assert subtract_1698(10, 4) == 6

def test_multiply_1699():
    assert multiply_1699(3, 7) == 21

def test_divide_1700():
    assert divide_1700(10, 2) == 5.0
