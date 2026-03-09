"""Tests for test module 494 — covers src modules [1973, 1974, 1975, 1976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1973 import modulo_1973
from module_1974 import power_1974
from module_1975 import min_1975
from module_1976 import max_1976

def test_modulo_1973():
    assert modulo_1973(10, 3) == 1

def test_power_1974():
    assert power_1974(2, 8) == 256

def test_min_1975():
    assert min_1975(3, 7) == 3

def test_max_1976():
    assert max_1976(3, 7) == 7
