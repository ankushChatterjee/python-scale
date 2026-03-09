"""Tests for test module 1325 — covers src modules [5297, 5298, 5299, 5300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5297 import add_5297
from module_5298 import subtract_5298
from module_5299 import multiply_5299
from module_5300 import divide_5300

def test_add_5297():
    assert add_5297(2, 3) == 5

def test_subtract_5298():
    assert subtract_5298(10, 4) == 6

def test_multiply_5299():
    assert multiply_5299(3, 7) == 21

def test_divide_5300():
    assert divide_5300(10, 2) == 5.0
