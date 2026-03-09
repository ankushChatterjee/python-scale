"""Tests for test module 865 — covers src modules [3457, 3458, 3459, 3460]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3457 import add_3457
from module_3458 import subtract_3458
from module_3459 import multiply_3459
from module_3460 import divide_3460

def test_add_3457():
    assert add_3457(2, 3) == 5

def test_subtract_3458():
    assert subtract_3458(10, 4) == 6

def test_multiply_3459():
    assert multiply_3459(3, 7) == 21

def test_divide_3460():
    assert divide_3460(10, 2) == 5.0
