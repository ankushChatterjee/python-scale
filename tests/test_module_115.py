"""Tests for module 115."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_115 import multiply_115, modulo_115, max_115, add_115

def test_multiply_115():
    assert multiply_115(3, 7) == 21

def test_modulo_115():
    assert modulo_115(10, 3) == 1

def test_max_115():
    assert max_115(3, 7) == 7

def test_add_115():
    assert add_115(2, 3) == 5
