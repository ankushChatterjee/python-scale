"""Tests for module 215."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_215 import multiply_215, subtract_215, modulo_215, max_215

def test_multiply_215():
    assert multiply_215(3, 7) == 21

def test_subtract_215():
    assert subtract_215(10, 4) == 6

def test_modulo_215():
    assert modulo_215(10, 3) == 1

def test_max_215():
    assert max_215(3, 7) == 7
