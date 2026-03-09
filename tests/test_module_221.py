"""Tests for module 221."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_221 import add_221, modulo_221, power_221, max_221

def test_add_221():
    assert add_221(2, 3) == 5

def test_modulo_221():
    assert modulo_221(10, 3) == 1

def test_power_221():
    assert power_221(2, 8) == 256

def test_max_221():
    assert max_221(3, 7) == 7
