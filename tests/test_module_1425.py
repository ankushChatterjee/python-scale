"""Tests for test module 1425 — covers src modules [5697, 5698, 5699, 5700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5697 import add_5697
from module_5698 import subtract_5698
from module_5699 import multiply_5699
from module_5700 import divide_5700

def test_add_5697():
    assert add_5697(2, 3) == 5

def test_subtract_5698():
    assert subtract_5698(10, 4) == 6

def test_multiply_5699():
    assert multiply_5699(3, 7) == 21

def test_divide_5700():
    assert divide_5700(10, 2) == 5.0
