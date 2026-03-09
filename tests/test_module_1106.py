"""Tests for test module 1106 — covers src modules [4421, 4422, 4423, 4424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4421 import modulo_4421
from module_4422 import power_4422
from module_4423 import min_4423
from module_4424 import max_4424

def test_modulo_4421():
    assert modulo_4421(10, 3) == 1

def test_power_4422():
    assert power_4422(2, 8) == 256

def test_min_4423():
    assert min_4423(3, 7) == 3

def test_max_4424():
    assert max_4424(3, 7) == 7
