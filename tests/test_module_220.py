"""Tests for module 220."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_220 import min_220, multiply_220, modulo_220, power_220

def test_min_220():
    assert min_220(3, 7) == 3

def test_multiply_220():
    assert multiply_220(3, 7) == 21

def test_modulo_220():
    assert modulo_220(10, 3) == 1

def test_power_220():
    assert power_220(2, 8) == 256
