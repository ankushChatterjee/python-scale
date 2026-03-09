"""Tests for test module 115 — covers src modules [457, 458, 459, 460]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_457 import add_457
from module_458 import subtract_458
from module_459 import multiply_459
from module_460 import divide_460

def test_add_457():
    assert add_457(2, 3) == 5

def test_subtract_458():
    assert subtract_458(10, 4) == 6

def test_multiply_459():
    assert multiply_459(3, 7) == 21

def test_divide_460():
    assert divide_460(10, 2) == 5.0
