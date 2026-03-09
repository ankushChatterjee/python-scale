"""Tests for test module 356 — covers src modules [1421, 1422, 1423, 1424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1421 import modulo_1421
from module_1422 import power_1422
from module_1423 import min_1423
from module_1424 import max_1424

def test_modulo_1421():
    assert modulo_1421(10, 3) == 1

def test_power_1422():
    assert power_1422(2, 8) == 256

def test_min_1423():
    assert min_1423(3, 7) == 3

def test_max_1424():
    assert max_1424(3, 7) == 7
