"""Tests for module 227."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_227 import modulo_227, power_227, divide_227, add_227

def test_modulo_227():
    assert modulo_227(10, 3) == 1

def test_power_227():
    assert power_227(2, 8) == 256

def test_divide_227():
    assert divide_227(10, 2) == 5.0

def test_add_227():
    assert add_227(2, 3) == 5
