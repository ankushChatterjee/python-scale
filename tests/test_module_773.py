"""Tests for test module 773 — covers src modules [3089, 3090, 3091, 3092]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3089 import add_3089
from module_3090 import subtract_3090
from module_3091 import multiply_3091
from module_3092 import divide_3092

def test_add_3089():
    assert add_3089(2, 3) == 5

def test_subtract_3090():
    assert subtract_3090(10, 4) == 6

def test_multiply_3091():
    assert multiply_3091(3, 7) == 21

def test_divide_3092():
    assert divide_3092(10, 2) == 5.0
