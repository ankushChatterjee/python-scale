"""Tests for test module 2269 — covers src modules [9073, 9074, 9075, 9076]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9073 import add_9073
from module_9074 import subtract_9074
from module_9075 import multiply_9075
from module_9076 import divide_9076

def test_add_9073():
    assert add_9073(2, 3) == 5

def test_subtract_9074():
    assert subtract_9074(10, 4) == 6

def test_multiply_9075():
    assert multiply_9075(3, 7) == 21

def test_divide_9076():
    assert divide_9076(10, 2) == 5.0
