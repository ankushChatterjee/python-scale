"""Tests for test module 1023 — covers src modules [4089, 4090, 4091, 4092]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4089 import add_4089
from module_4090 import subtract_4090
from module_4091 import multiply_4091
from module_4092 import divide_4092

def test_add_4089():
    assert add_4089(2, 3) == 5

def test_subtract_4090():
    assert subtract_4090(10, 4) == 6

def test_multiply_4091():
    assert multiply_4091(3, 7) == 21

def test_divide_4092():
    assert divide_4092(10, 2) == 5.0
