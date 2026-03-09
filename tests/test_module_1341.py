"""Tests for test module 1341 — covers src modules [5361, 5362, 5363, 5364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5361 import add_5361
from module_5362 import subtract_5362
from module_5363 import multiply_5363
from module_5364 import divide_5364

def test_add_5361():
    assert add_5361(2, 3) == 5

def test_subtract_5362():
    assert subtract_5362(10, 4) == 6

def test_multiply_5363():
    assert multiply_5363(3, 7) == 21

def test_divide_5364():
    assert divide_5364(10, 2) == 5.0
