"""Tests for module 117."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_117 import power_117, divide_117, modulo_117, max_117

def test_power_117():
    assert power_117(2, 8) == 256

def test_divide_117():
    assert divide_117(10, 2) == 5.0

def test_modulo_117():
    assert modulo_117(10, 3) == 1

def test_max_117():
    assert max_117(3, 7) == 7
