"""Tests for test module 1480 — covers src modules [5917, 5918, 5919, 5920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5917 import modulo_5917
from module_5918 import power_5918
from module_5919 import min_5919
from module_5920 import max_5920

def test_modulo_5917():
    assert modulo_5917(10, 3) == 1

def test_power_5918():
    assert power_5918(2, 8) == 256

def test_min_5919():
    assert min_5919(3, 7) == 3

def test_max_5920():
    assert max_5920(3, 7) == 7
