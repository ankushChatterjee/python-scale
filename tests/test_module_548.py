"""Tests for test module 548 — covers src modules [2189, 2190, 2191, 2192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2189 import modulo_2189
from module_2190 import power_2190
from module_2191 import min_2191
from module_2192 import max_2192

def test_modulo_2189():
    assert modulo_2189(10, 3) == 1

def test_power_2190():
    assert power_2190(2, 8) == 256

def test_min_2191():
    assert min_2191(3, 7) == 3

def test_max_2192():
    assert max_2192(3, 7) == 7
