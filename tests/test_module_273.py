"""Tests for test module 273 — covers src modules [1089, 1090, 1091, 1092]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1089 import add_1089
from module_1090 import subtract_1090
from module_1091 import multiply_1091
from module_1092 import divide_1092

def test_add_1089():
    assert add_1089(2, 3) == 5

def test_subtract_1090():
    assert subtract_1090(10, 4) == 6

def test_multiply_1091():
    assert multiply_1091(3, 7) == 21

def test_divide_1092():
    assert divide_1092(10, 2) == 5.0
