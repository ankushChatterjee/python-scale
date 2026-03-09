"""Tests for test module 269 — covers src modules [1073, 1074, 1075, 1076]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1073 import add_1073
from module_1074 import subtract_1074
from module_1075 import multiply_1075
from module_1076 import divide_1076

def test_add_1073():
    assert add_1073(2, 3) == 5

def test_subtract_1074():
    assert subtract_1074(10, 4) == 6

def test_multiply_1075():
    assert multiply_1075(3, 7) == 21

def test_divide_1076():
    assert divide_1076(10, 2) == 5.0
