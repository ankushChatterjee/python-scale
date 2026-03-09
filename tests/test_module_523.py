"""Tests for test module 523 — covers src modules [2089, 2090, 2091, 2092]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2089 import add_2089
from module_2090 import subtract_2090
from module_2091 import multiply_2091
from module_2092 import divide_2092

def test_add_2089():
    assert add_2089(2, 3) == 5

def test_subtract_2090():
    assert subtract_2090(10, 4) == 6

def test_multiply_2091():
    assert multiply_2091(3, 7) == 21

def test_divide_2092():
    assert divide_2092(10, 2) == 5.0
