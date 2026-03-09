"""Tests for module 202."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_202 import divide_202, multiply_202, add_202, modulo_202

def test_divide_202():
    assert divide_202(10, 2) == 5.0

def test_multiply_202():
    assert multiply_202(3, 7) == 21

def test_add_202():
    assert add_202(2, 3) == 5

def test_modulo_202():
    assert modulo_202(10, 3) == 1
