"""Tests for module 153."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_153 import min_153, divide_153, modulo_153, add_153

def test_min_153():
    assert min_153(3, 7) == 3

def test_divide_153():
    assert divide_153(10, 2) == 5.0

def test_modulo_153():
    assert modulo_153(10, 3) == 1

def test_add_153():
    assert add_153(2, 3) == 5
