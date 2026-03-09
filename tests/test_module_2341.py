"""Tests for test module 2341 — covers src modules [9361, 9362, 9363, 9364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9361 import add_9361
from module_9362 import subtract_9362
from module_9363 import multiply_9363
from module_9364 import divide_9364

def test_add_9361():
    assert add_9361(2, 3) == 5

def test_subtract_9362():
    assert subtract_9362(10, 4) == 6

def test_multiply_9363():
    assert multiply_9363(3, 7) == 21

def test_divide_9364():
    assert divide_9364(10, 2) == 5.0
