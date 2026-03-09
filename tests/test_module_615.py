"""Tests for test module 615 — covers src modules [2457, 2458, 2459, 2460]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2457 import add_2457
from module_2458 import subtract_2458
from module_2459 import multiply_2459
from module_2460 import divide_2460

def test_add_2457():
    assert add_2457(2, 3) == 5

def test_subtract_2458():
    assert subtract_2458(10, 4) == 6

def test_multiply_2459():
    assert multiply_2459(3, 7) == 21

def test_divide_2460():
    assert divide_2460(10, 2) == 5.0
