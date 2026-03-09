"""Tests for test module 2091 — covers src modules [8361, 8362, 8363, 8364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8361 import add_8361
from module_8362 import subtract_8362
from module_8363 import multiply_8363
from module_8364 import divide_8364

def test_add_8361():
    assert add_8361(2, 3) == 5

def test_subtract_8362():
    assert subtract_8362(10, 4) == 6

def test_multiply_8363():
    assert multiply_8363(3, 7) == 21

def test_divide_8364():
    assert divide_8364(10, 2) == 5.0
