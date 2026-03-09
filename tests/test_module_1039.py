"""Tests for test module 1039 — covers src modules [4153, 4154, 4155, 4156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4153 import add_4153
from module_4154 import subtract_4154
from module_4155 import multiply_4155
from module_4156 import divide_4156

def test_add_4153():
    assert add_4153(2, 3) == 5

def test_subtract_4154():
    assert subtract_4154(10, 4) == 6

def test_multiply_4155():
    assert multiply_4155(3, 7) == 21

def test_divide_4156():
    assert divide_4156(10, 2) == 5.0
