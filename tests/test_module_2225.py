"""Tests for test module 2225 — covers src modules [8897, 8898, 8899, 8900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8897 import add_8897
from module_8898 import subtract_8898
from module_8899 import multiply_8899
from module_8900 import divide_8900

def test_add_8897():
    assert add_8897(2, 3) == 5

def test_subtract_8898():
    assert subtract_8898(10, 4) == 6

def test_multiply_8899():
    assert multiply_8899(3, 7) == 21

def test_divide_8900():
    assert divide_8900(10, 2) == 5.0
