"""Tests for test module 1091 — covers src modules [4361, 4362, 4363, 4364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4361 import add_4361
from module_4362 import subtract_4362
from module_4363 import multiply_4363
from module_4364 import divide_4364

def test_add_4361():
    assert add_4361(2, 3) == 5

def test_subtract_4362():
    assert subtract_4362(10, 4) == 6

def test_multiply_4363():
    assert multiply_4363(3, 7) == 21

def test_divide_4364():
    assert divide_4364(10, 2) == 5.0
