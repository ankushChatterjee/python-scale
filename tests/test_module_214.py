"""Tests for module 214."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_214 import max_214, add_214, modulo_214, min_214

def test_max_214():
    assert max_214(3, 7) == 7

def test_add_214():
    assert add_214(2, 3) == 5

def test_modulo_214():
    assert modulo_214(10, 3) == 1

def test_min_214():
    assert min_214(3, 7) == 3
