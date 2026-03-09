"""Tests for module 198."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_198 import max_198, modulo_198, min_198, multiply_198

def test_max_198():
    assert max_198(3, 7) == 7

def test_modulo_198():
    assert modulo_198(10, 3) == 1

def test_min_198():
    assert min_198(3, 7) == 3

def test_multiply_198():
    assert multiply_198(3, 7) == 21
