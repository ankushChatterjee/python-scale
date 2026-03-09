"""Tests for test module 845 — covers src modules [3377, 3378, 3379, 3380]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3377 import add_3377
from module_3378 import subtract_3378
from module_3379 import multiply_3379
from module_3380 import divide_3380

def test_add_3377():
    assert add_3377(2, 3) == 5

def test_subtract_3378():
    assert subtract_3378(10, 4) == 6

def test_multiply_3379():
    assert multiply_3379(3, 7) == 21

def test_divide_3380():
    assert divide_3380(10, 2) == 5.0
