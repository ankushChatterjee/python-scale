"""Tests for module 211."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_211 import modulo_211, divide_211, min_211, power_211

def test_modulo_211():
    assert modulo_211(10, 3) == 1

def test_divide_211():
    assert divide_211(10, 2) == 5.0

def test_min_211():
    assert min_211(3, 7) == 3

def test_power_211():
    assert power_211(2, 8) == 256
