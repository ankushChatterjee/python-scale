"""Tests for test module 1856 — covers src modules [7421, 7422, 7423, 7424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7421 import modulo_7421
from module_7422 import power_7422
from module_7423 import min_7423
from module_7424 import max_7424

def test_modulo_7421():
    assert modulo_7421(10, 3) == 1

def test_power_7422():
    assert power_7422(2, 8) == 256

def test_min_7423():
    assert min_7423(3, 7) == 3

def test_max_7424():
    assert max_7424(3, 7) == 7
