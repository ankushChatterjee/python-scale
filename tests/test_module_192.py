"""Tests for module 192."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_192 import add_192, modulo_192, subtract_192, max_192

def test_add_192():
    assert add_192(2, 3) == 5

def test_modulo_192():
    assert modulo_192(10, 3) == 1

def test_subtract_192():
    assert subtract_192(10, 4) == 6

def test_max_192():
    assert max_192(3, 7) == 7
