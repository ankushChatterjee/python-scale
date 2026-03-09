"""Tests for test module 1675 — covers src modules [6697, 6698, 6699, 6700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6697 import add_6697
from module_6698 import subtract_6698
from module_6699 import multiply_6699
from module_6700 import divide_6700

def test_add_6697():
    assert add_6697(2, 3) == 5

def test_subtract_6698():
    assert subtract_6698(10, 4) == 6

def test_multiply_6699():
    assert multiply_6699(3, 7) == 21

def test_divide_6700():
    assert divide_6700(10, 2) == 5.0
