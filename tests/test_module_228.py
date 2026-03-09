"""Tests for module 228."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_228 import divide_228, multiply_228, power_228, modulo_228

def test_divide_228():
    assert divide_228(10, 2) == 5.0

def test_multiply_228():
    assert multiply_228(3, 7) == 21

def test_power_228():
    assert power_228(2, 8) == 256

def test_modulo_228():
    assert modulo_228(10, 3) == 1
