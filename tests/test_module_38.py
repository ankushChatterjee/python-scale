"""Tests for module 38."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_38 import multiply_38, modulo_38, add_38, max_38

def test_multiply_38():
    assert multiply_38(3, 7) == 21

def test_modulo_38():
    assert modulo_38(10, 3) == 1

def test_add_38():
    assert add_38(2, 3) == 5

def test_max_38():
    assert max_38(3, 7) == 7
