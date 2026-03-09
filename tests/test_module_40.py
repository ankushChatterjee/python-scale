"""Tests for module 40."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_40 import add_40, modulo_40, multiply_40, divide_40

def test_add_40():
    assert add_40(2, 3) == 5

def test_modulo_40():
    assert modulo_40(10, 3) == 1

def test_multiply_40():
    assert multiply_40(3, 7) == 21

def test_divide_40():
    assert divide_40(10, 2) == 5.0
