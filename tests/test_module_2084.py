"""Tests for test module 2084 — covers src modules [8333, 8334, 8335, 8336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8333 import modulo_8333
from module_8334 import power_8334
from module_8335 import min_8335
from module_8336 import max_8336

def test_modulo_8333():
    assert modulo_8333(10, 3) == 1

def test_power_8334():
    assert power_8334(2, 8) == 256

def test_min_8335():
    assert min_8335(3, 7) == 3

def test_max_8336():
    assert max_8336(3, 7) == 7
