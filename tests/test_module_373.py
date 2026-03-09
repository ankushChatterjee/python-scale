"""Tests for test module 373 — covers src modules [1489, 1490, 1491, 1492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1489 import add_1489
from module_1490 import subtract_1490
from module_1491 import multiply_1491
from module_1492 import divide_1492

def test_add_1489():
    assert add_1489(2, 3) == 5

def test_subtract_1490():
    assert subtract_1490(10, 4) == 6

def test_multiply_1491():
    assert multiply_1491(3, 7) == 21

def test_divide_1492():
    assert divide_1492(10, 2) == 5.0
