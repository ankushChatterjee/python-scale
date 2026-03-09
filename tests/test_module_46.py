"""Tests for module 46."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_46 import multiply_46, max_46, modulo_46, power_46

def test_multiply_46():
    assert multiply_46(3, 7) == 21

def test_max_46():
    assert max_46(3, 7) == 7

def test_modulo_46():
    assert modulo_46(10, 3) == 1

def test_power_46():
    assert power_46(2, 8) == 256
