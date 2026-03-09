"""Tests for test module 1289 — covers src modules [5153, 5154, 5155, 5156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5153 import add_5153
from module_5154 import subtract_5154
from module_5155 import multiply_5155
from module_5156 import divide_5156

def test_add_5153():
    assert add_5153(2, 3) == 5

def test_subtract_5154():
    assert subtract_5154(10, 4) == 6

def test_multiply_5155():
    assert multiply_5155(3, 7) == 21

def test_divide_5156():
    assert divide_5156(10, 2) == 5.0
