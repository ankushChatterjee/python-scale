"""Tests for test module 856 — covers src modules [3421, 3422, 3423, 3424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3421 import modulo_3421
from module_3422 import power_3422
from module_3423 import min_3423
from module_3424 import max_3424

def test_modulo_3421():
    assert modulo_3421(10, 3) == 1

def test_power_3422():
    assert power_3422(2, 8) == 256

def test_min_3423():
    assert min_3423(3, 7) == 3

def test_max_3424():
    assert max_3424(3, 7) == 7
