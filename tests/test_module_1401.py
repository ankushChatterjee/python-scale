"""Tests for test module 1401 — covers src modules [5601, 5602, 5603, 5604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5601 import add_5601
from module_5602 import subtract_5602
from module_5603 import multiply_5603
from module_5604 import divide_5604

def test_add_5601():
    assert add_5601(2, 3) == 5

def test_subtract_5602():
    assert subtract_5602(10, 4) == 6

def test_multiply_5603():
    assert multiply_5603(3, 7) == 21

def test_divide_5604():
    assert divide_5604(10, 2) == 5.0
