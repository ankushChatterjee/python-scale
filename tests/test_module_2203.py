"""Tests for test module 2203 — covers src modules [8809, 8810, 8811, 8812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8809 import add_8809
from module_8810 import subtract_8810
from module_8811 import multiply_8811
from module_8812 import divide_8812

def test_add_8809():
    assert add_8809(2, 3) == 5

def test_subtract_8810():
    assert subtract_8810(10, 4) == 6

def test_multiply_8811():
    assert multiply_8811(3, 7) == 21

def test_divide_8812():
    assert divide_8812(10, 2) == 5.0
