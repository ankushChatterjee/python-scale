"""Tests for test module 834 — covers src modules [3333, 3334, 3335, 3336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3333 import modulo_3333
from module_3334 import power_3334
from module_3335 import min_3335
from module_3336 import max_3336

def test_modulo_3333():
    assert modulo_3333(10, 3) == 1

def test_power_3334():
    assert power_3334(2, 8) == 256

def test_min_3335():
    assert min_3335(3, 7) == 3

def test_max_3336():
    assert max_3336(3, 7) == 7
