"""Tests for test module 1175 — covers src modules [4697, 4698, 4699, 4700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4697 import add_4697
from module_4698 import subtract_4698
from module_4699 import multiply_4699
from module_4700 import divide_4700

def test_add_4697():
    assert add_4697(2, 3) == 5

def test_subtract_4698():
    assert subtract_4698(10, 4) == 6

def test_multiply_4699():
    assert multiply_4699(3, 7) == 21

def test_divide_4700():
    assert divide_4700(10, 2) == 5.0
