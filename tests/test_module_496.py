"""Tests for test module 496 — covers src modules [1981, 1982, 1983, 1984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1981 import modulo_1981
from module_1982 import power_1982
from module_1983 import min_1983
from module_1984 import max_1984

def test_modulo_1981():
    assert modulo_1981(10, 3) == 1

def test_power_1982():
    assert power_1982(2, 8) == 256

def test_min_1983():
    assert min_1983(3, 7) == 3

def test_max_1984():
    assert max_1984(3, 7) == 7
