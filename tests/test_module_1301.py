"""Tests for test module 1301 — covers src modules [5201, 5202, 5203, 5204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5201 import add_5201
from module_5202 import subtract_5202
from module_5203 import multiply_5203
from module_5204 import divide_5204

def test_add_5201():
    assert add_5201(2, 3) == 5

def test_subtract_5202():
    assert subtract_5202(10, 4) == 6

def test_multiply_5203():
    assert multiply_5203(3, 7) == 21

def test_divide_5204():
    assert divide_5204(10, 2) == 5.0
