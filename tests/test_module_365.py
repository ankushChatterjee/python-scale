"""Tests for test module 365 — covers src modules [1457, 1458, 1459, 1460]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1457 import add_1457
from module_1458 import subtract_1458
from module_1459 import multiply_1459
from module_1460 import divide_1460

def test_add_1457():
    assert add_1457(2, 3) == 5

def test_subtract_1458():
    assert subtract_1458(10, 4) == 6

def test_multiply_1459():
    assert multiply_1459(3, 7) == 21

def test_divide_1460():
    assert divide_1460(10, 2) == 5.0
