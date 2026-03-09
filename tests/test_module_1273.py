"""Tests for test module 1273 — covers src modules [5089, 5090, 5091, 5092]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5089 import add_5089
from module_5090 import subtract_5090
from module_5091 import multiply_5091
from module_5092 import divide_5092

def test_add_5089():
    assert add_5089(2, 3) == 5

def test_subtract_5090():
    assert subtract_5090(10, 4) == 6

def test_multiply_5091():
    assert multiply_5091(3, 7) == 21

def test_divide_5092():
    assert divide_5092(10, 2) == 5.0
