"""Tests for test module 1865 — covers src modules [7457, 7458, 7459, 7460]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7457 import add_7457
from module_7458 import subtract_7458
from module_7459 import multiply_7459
from module_7460 import divide_7460

def test_add_7457():
    assert add_7457(2, 3) == 5

def test_subtract_7458():
    assert subtract_7458(10, 4) == 6

def test_multiply_7459():
    assert multiply_7459(3, 7) == 21

def test_divide_7460():
    assert divide_7460(10, 2) == 5.0
