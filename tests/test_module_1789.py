"""Tests for test module 1789 — covers src modules [7153, 7154, 7155, 7156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7153 import add_7153
from module_7154 import subtract_7154
from module_7155 import multiply_7155
from module_7156 import divide_7156

def test_add_7153():
    assert add_7153(2, 3) == 5

def test_subtract_7154():
    assert subtract_7154(10, 4) == 6

def test_multiply_7155():
    assert multiply_7155(3, 7) == 21

def test_divide_7156():
    assert divide_7156(10, 2) == 5.0
