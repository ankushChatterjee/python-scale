"""Tests for test module 225 — covers src modules [897, 898, 899, 900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_897 import add_897
from module_898 import subtract_898
from module_899 import multiply_899
from module_900 import divide_900

def test_add_897():
    assert add_897(2, 3) == 5

def test_subtract_898():
    assert subtract_898(10, 4) == 6

def test_multiply_899():
    assert multiply_899(3, 7) == 21

def test_divide_900():
    assert divide_900(10, 2) == 5.0
