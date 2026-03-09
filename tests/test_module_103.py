"""Tests for module 103."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_103 import power_103, min_103, modulo_103, divide_103

def test_power_103():
    assert power_103(2, 8) == 256

def test_min_103():
    assert min_103(3, 7) == 3

def test_modulo_103():
    assert modulo_103(10, 3) == 1

def test_divide_103():
    assert divide_103(10, 2) == 5.0
