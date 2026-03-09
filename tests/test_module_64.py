"""Tests for module 64."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_64 import max_64, min_64, modulo_64, add_64

def test_max_64():
    assert max_64(3, 7) == 7

def test_min_64():
    assert min_64(3, 7) == 3

def test_modulo_64():
    assert modulo_64(10, 3) == 1

def test_add_64():
    assert add_64(2, 3) == 5
