"""Tests for module 65."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_65 import add_65, power_65, modulo_65, max_65

def test_add_65():
    assert add_65(2, 3) == 5

def test_power_65():
    assert power_65(2, 8) == 256

def test_modulo_65():
    assert modulo_65(10, 3) == 1

def test_max_65():
    assert max_65(3, 7) == 7
