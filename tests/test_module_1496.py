"""Tests for test module 1496 — covers src modules [5981, 5982, 5983, 5984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5981 import modulo_5981
from module_5982 import power_5982
from module_5983 import min_5983
from module_5984 import max_5984

def test_modulo_5981():
    assert modulo_5981(10, 3) == 1

def test_power_5982():
    assert power_5982(2, 8) == 256

def test_min_5983():
    assert min_5983(3, 7) == 3

def test_max_5984():
    assert max_5984(3, 7) == 7
