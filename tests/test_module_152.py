"""Tests for module 152."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_152 import max_152, divide_152, add_152, subtract_152

def test_max_152():
    assert max_152(3, 7) == 7

def test_divide_152():
    assert divide_152(10, 2) == 5.0

def test_add_152():
    assert add_152(2, 3) == 5

def test_subtract_152():
    assert subtract_152(10, 4) == 6
