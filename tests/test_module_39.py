"""Tests for test module 39 — covers src modules [153, 154, 155, 156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_153 import add_153
from module_154 import subtract_154
from module_155 import multiply_155
from module_156 import divide_156

def test_add_153():
    assert add_153(2, 3) == 5

def test_subtract_154():
    assert subtract_154(10, 4) == 6

def test_multiply_155():
    assert multiply_155(3, 7) == 21

def test_divide_156():
    assert divide_156(10, 2) == 5.0
