"""Tests for module 84."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_84 import subtract_84, add_84, modulo_84, max_84

def test_subtract_84():
    assert subtract_84(10, 4) == 6

def test_add_84():
    assert add_84(2, 3) == 5

def test_modulo_84():
    assert modulo_84(10, 3) == 1

def test_max_84():
    assert max_84(3, 7) == 7
