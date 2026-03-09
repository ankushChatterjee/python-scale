"""Tests for test module 289 — covers src modules [1153, 1154, 1155, 1156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1153 import add_1153
from module_1154 import subtract_1154
from module_1155 import multiply_1155
from module_1156 import divide_1156

def test_add_1153():
    assert add_1153(2, 3) == 5

def test_subtract_1154():
    assert subtract_1154(10, 4) == 6

def test_multiply_1155():
    assert multiply_1155(3, 7) == 21

def test_divide_1156():
    assert divide_1156(10, 2) == 5.0
