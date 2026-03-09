"""Tests for test module 1615 — covers src modules [6457, 6458, 6459, 6460]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6457 import add_6457
from module_6458 import subtract_6458
from module_6459 import multiply_6459
from module_6460 import divide_6460

def test_add_6457():
    assert add_6457(2, 3) == 5

def test_subtract_6458():
    assert subtract_6458(10, 4) == 6

def test_multiply_6459():
    assert multiply_6459(3, 7) == 21

def test_divide_6460():
    assert divide_6460(10, 2) == 5.0
