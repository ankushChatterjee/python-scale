"""Tests for test module 1901 — covers src modules [7601, 7602, 7603, 7604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7601 import add_7601
from module_7602 import subtract_7602
from module_7603 import multiply_7603
from module_7604 import divide_7604

def test_add_7601():
    assert add_7601(2, 3) == 5

def test_subtract_7602():
    assert subtract_7602(10, 4) == 6

def test_multiply_7603():
    assert multiply_7603(3, 7) == 21

def test_divide_7604():
    assert divide_7604(10, 2) == 5.0
