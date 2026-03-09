"""Tests for test module 1539 — covers src modules [6153, 6154, 6155, 6156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6153 import add_6153
from module_6154 import subtract_6154
from module_6155 import multiply_6155
from module_6156 import divide_6156

def test_add_6153():
    assert add_6153(2, 3) == 5

def test_subtract_6154():
    assert subtract_6154(10, 4) == 6

def test_multiply_6155():
    assert multiply_6155(3, 7) == 21

def test_divide_6156():
    assert divide_6156(10, 2) == 5.0
