"""Tests for test module 1773 — covers src modules [7089, 7090, 7091, 7092]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7089 import add_7089
from module_7090 import subtract_7090
from module_7091 import multiply_7091
from module_7092 import divide_7092

def test_add_7089():
    assert add_7089(2, 3) == 5

def test_subtract_7090():
    assert subtract_7090(10, 4) == 6

def test_multiply_7091():
    assert multiply_7091(3, 7) == 21

def test_divide_7092():
    assert divide_7092(10, 2) == 5.0
