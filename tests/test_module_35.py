"""Tests for module 35."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_35 import modulo_35, min_35, power_35, multiply_35

def test_modulo_35():
    assert modulo_35(10, 3) == 1

def test_min_35():
    assert min_35(3, 7) == 3

def test_power_35():
    assert power_35(2, 8) == 256

def test_multiply_35():
    assert multiply_35(3, 7) == 21
