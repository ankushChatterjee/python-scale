"""Tests for test module 1834 — covers src modules [7333, 7334, 7335, 7336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7333 import modulo_7333
from module_7334 import power_7334
from module_7335 import min_7335
from module_7336 import max_7336

def test_modulo_7333():
    assert modulo_7333(10, 3) == 1

def test_power_7334():
    assert power_7334(2, 8) == 256

def test_min_7335():
    assert min_7335(3, 7) == 3

def test_max_7336():
    assert max_7336(3, 7) == 7
