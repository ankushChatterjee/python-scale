"""Tests for test module 1349 — covers src modules [5393, 5394, 5395, 5396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5393 import add_5393
from module_5394 import subtract_5394
from module_5395 import multiply_5395
from module_5396 import divide_5396

def test_add_5393():
    assert add_5393(2, 3) == 5

def test_subtract_5394():
    assert subtract_5394(10, 4) == 6

def test_multiply_5395():
    assert multiply_5395(3, 7) == 21

def test_divide_5396():
    assert divide_5396(10, 2) == 5.0
