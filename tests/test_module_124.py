"""Tests for module 124."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_124 import min_124, power_124, multiply_124, modulo_124

def test_min_124():
    assert min_124(3, 7) == 3

def test_power_124():
    assert power_124(2, 8) == 256

def test_multiply_124():
    assert multiply_124(3, 7) == 21

def test_modulo_124():
    assert modulo_124(10, 3) == 1
