"""Tests for test module 106 — covers src modules [421, 422, 423, 424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_421 import modulo_421
from module_422 import power_422
from module_423 import min_423
from module_424 import max_424

def test_modulo_421():
    assert modulo_421(10, 3) == 1

def test_power_422():
    assert power_422(2, 8) == 256

def test_min_423():
    assert min_423(3, 7) == 3

def test_max_424():
    assert max_424(3, 7) == 7
