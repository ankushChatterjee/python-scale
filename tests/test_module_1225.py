"""Tests for test module 1225 — covers src modules [4897, 4898, 4899, 4900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4897 import add_4897
from module_4898 import subtract_4898
from module_4899 import multiply_4899
from module_4900 import divide_4900

def test_add_4897():
    assert add_4897(2, 3) == 5

def test_subtract_4898():
    assert subtract_4898(10, 4) == 6

def test_multiply_4899():
    assert multiply_4899(3, 7) == 21

def test_divide_4900():
    assert divide_4900(10, 2) == 5.0
