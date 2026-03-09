"""Tests for module 97."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_97 import min_97, modulo_97, add_97, power_97

def test_min_97():
    assert min_97(3, 7) == 3

def test_modulo_97():
    assert modulo_97(10, 3) == 1

def test_add_97():
    assert add_97(2, 3) == 5

def test_power_97():
    assert power_97(2, 8) == 256
