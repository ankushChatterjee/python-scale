"""Tests for test module 1523 — covers src modules [6089, 6090, 6091, 6092]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6089 import add_6089
from module_6090 import subtract_6090
from module_6091 import multiply_6091
from module_6092 import divide_6092

def test_add_6089():
    assert add_6089(2, 3) == 5

def test_subtract_6090():
    assert subtract_6090(10, 4) == 6

def test_multiply_6091():
    assert multiply_6091(3, 7) == 21

def test_divide_6092():
    assert divide_6092(10, 2) == 5.0
