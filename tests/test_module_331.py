"""Tests for test module 331 — covers src modules [1321, 1322, 1323, 1324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1321 import add_1321
from module_1322 import subtract_1322
from module_1323 import multiply_1323
from module_1324 import divide_1324

def test_add_1321():
    assert add_1321(2, 3) == 5

def test_subtract_1322():
    assert subtract_1322(10, 4) == 6

def test_multiply_1323():
    assert multiply_1323(3, 7) == 21

def test_divide_1324():
    assert divide_1324(10, 2) == 5.0
