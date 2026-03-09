"""Tests for test module 1841 — covers src modules [7361, 7362, 7363, 7364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7361 import add_7361
from module_7362 import subtract_7362
from module_7363 import multiply_7363
from module_7364 import divide_7364

def test_add_7361():
    assert add_7361(2, 3) == 5

def test_subtract_7362():
    assert subtract_7362(10, 4) == 6

def test_multiply_7363():
    assert multiply_7363(3, 7) == 21

def test_divide_7364():
    assert divide_7364(10, 2) == 5.0
