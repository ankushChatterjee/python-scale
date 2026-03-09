"""Tests for module 247."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_247 import modulo_247, multiply_247, add_247, divide_247

def test_modulo_247():
    assert modulo_247(10, 3) == 1

def test_multiply_247():
    assert multiply_247(3, 7) == 21

def test_add_247():
    assert add_247(2, 3) == 5

def test_divide_247():
    assert divide_247(10, 2) == 5.0
