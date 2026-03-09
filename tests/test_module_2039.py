"""Tests for test module 2039 — covers src modules [8153, 8154, 8155, 8156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8153 import add_8153
from module_8154 import subtract_8154
from module_8155 import multiply_8155
from module_8156 import divide_8156

def test_add_8153():
    assert add_8153(2, 3) == 5

def test_subtract_8154():
    assert subtract_8154(10, 4) == 6

def test_multiply_8155():
    assert multiply_8155(3, 7) == 21

def test_divide_8156():
    assert divide_8156(10, 2) == 5.0
