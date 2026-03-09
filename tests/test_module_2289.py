"""Tests for test module 2289 — covers src modules [9153, 9154, 9155, 9156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9153 import add_9153
from module_9154 import subtract_9154
from module_9155 import multiply_9155
from module_9156 import divide_9156

def test_add_9153():
    assert add_9153(2, 3) == 5

def test_subtract_9154():
    assert subtract_9154(10, 4) == 6

def test_multiply_9155():
    assert multiply_9155(3, 7) == 21

def test_divide_9156():
    assert divide_9156(10, 2) == 5.0
