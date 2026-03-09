"""Tests for test module 84 — covers src modules [333, 334, 335, 336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_333 import modulo_333
from module_334 import power_334
from module_335 import min_335
from module_336 import max_336

def test_modulo_333():
    assert modulo_333(10, 3) == 1

def test_power_334():
    assert power_334(2, 8) == 256

def test_min_335():
    assert min_335(3, 7) == 3

def test_max_336():
    assert max_336(3, 7) == 7
