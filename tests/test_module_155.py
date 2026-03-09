"""Tests for module 155."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_155 import modulo_155, min_155, divide_155, power_155

def test_modulo_155():
    assert modulo_155(10, 3) == 1

def test_min_155():
    assert min_155(3, 7) == 3

def test_divide_155():
    assert divide_155(10, 2) == 5.0

def test_power_155():
    assert power_155(2, 8) == 256
