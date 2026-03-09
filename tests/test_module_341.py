"""Tests for test module 341 — covers src modules [1361, 1362, 1363, 1364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1361 import add_1361
from module_1362 import subtract_1362
from module_1363 import multiply_1363
from module_1364 import divide_1364

def test_add_1361():
    assert add_1361(2, 3) == 5

def test_subtract_1362():
    assert subtract_1362(10, 4) == 6

def test_multiply_1363():
    assert multiply_1363(3, 7) == 21

def test_divide_1364():
    assert divide_1364(10, 2) == 5.0
