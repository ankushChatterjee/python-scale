"""Tests for module 113."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_113 import power_113, max_113, modulo_113, divide_113

def test_power_113():
    assert power_113(2, 8) == 256

def test_max_113():
    assert max_113(3, 7) == 7

def test_modulo_113():
    assert modulo_113(10, 3) == 1

def test_divide_113():
    assert divide_113(10, 2) == 5.0
