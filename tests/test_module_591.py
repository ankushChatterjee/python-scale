"""Tests for test module 591 — covers src modules [2361, 2362, 2363, 2364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2361 import add_2361
from module_2362 import subtract_2362
from module_2363 import multiply_2363
from module_2364 import divide_2364

def test_add_2361():
    assert add_2361(2, 3) == 5

def test_subtract_2362():
    assert subtract_2362(10, 4) == 6

def test_multiply_2363():
    assert multiply_2363(3, 7) == 21

def test_divide_2364():
    assert divide_2364(10, 2) == 5.0
