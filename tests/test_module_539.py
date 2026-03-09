"""Tests for test module 539 — covers src modules [2153, 2154, 2155, 2156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2153 import add_2153
from module_2154 import subtract_2154
from module_2155 import multiply_2155
from module_2156 import divide_2156

def test_add_2153():
    assert add_2153(2, 3) == 5

def test_subtract_2154():
    assert subtract_2154(10, 4) == 6

def test_multiply_2155():
    assert multiply_2155(3, 7) == 21

def test_divide_2156():
    assert divide_2156(10, 2) == 5.0
