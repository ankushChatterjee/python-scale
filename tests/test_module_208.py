"""Tests for module 208."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_208 import modulo_208, add_208, min_208, max_208

def test_modulo_208():
    assert modulo_208(10, 3) == 1

def test_add_208():
    assert add_208(2, 3) == 5

def test_min_208():
    assert min_208(3, 7) == 3

def test_max_208():
    assert max_208(3, 7) == 7
