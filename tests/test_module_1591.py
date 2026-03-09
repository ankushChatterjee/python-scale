"""Tests for test module 1591 — covers src modules [6361, 6362, 6363, 6364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6361 import add_6361
from module_6362 import subtract_6362
from module_6363 import multiply_6363
from module_6364 import divide_6364

def test_add_6361():
    assert add_6361(2, 3) == 5

def test_subtract_6362():
    assert subtract_6362(10, 4) == 6

def test_multiply_6363():
    assert multiply_6363(3, 7) == 21

def test_divide_6364():
    assert divide_6364(10, 2) == 5.0
