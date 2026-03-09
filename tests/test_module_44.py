"""Tests for module 44."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_44 import subtract_44, min_44, modulo_44, max_44

def test_subtract_44():
    assert subtract_44(10, 4) == 6

def test_min_44():
    assert min_44(3, 7) == 3

def test_modulo_44():
    assert modulo_44(10, 3) == 1

def test_max_44():
    assert max_44(3, 7) == 7
