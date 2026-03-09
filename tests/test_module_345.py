"""Tests for test module 345 — covers src modules [1377, 1378, 1379, 1380]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1377 import add_1377
from module_1378 import subtract_1378
from module_1379 import multiply_1379
from module_1380 import divide_1380

def test_add_1377():
    assert add_1377(2, 3) == 5

def test_subtract_1378():
    assert subtract_1378(10, 4) == 6

def test_multiply_1379():
    assert multiply_1379(3, 7) == 21

def test_divide_1380():
    assert divide_1380(10, 2) == 5.0
