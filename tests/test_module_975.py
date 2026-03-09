"""Tests for test module 975 — covers src modules [3897, 3898, 3899, 3900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3897 import add_3897
from module_3898 import subtract_3898
from module_3899 import multiply_3899
from module_3900 import divide_3900

def test_add_3897():
    assert add_3897(2, 3) == 5

def test_subtract_3898():
    assert subtract_3898(10, 4) == 6

def test_multiply_3899():
    assert multiply_3899(3, 7) == 21

def test_divide_3900():
    assert divide_3900(10, 2) == 5.0
