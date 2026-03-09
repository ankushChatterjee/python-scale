"""Tests for test module 841 — covers src modules [3361, 3362, 3363, 3364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3361 import add_3361
from module_3362 import subtract_3362
from module_3363 import multiply_3363
from module_3364 import divide_3364

def test_add_3361():
    assert add_3361(2, 3) == 5

def test_subtract_3362():
    assert subtract_3362(10, 4) == 6

def test_multiply_3363():
    assert multiply_3363(3, 7) == 21

def test_divide_3364():
    assert divide_3364(10, 2) == 5.0
