"""Tests for test module 2244 — covers src modules [8973, 8974, 8975, 8976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8973 import modulo_8973
from module_8974 import power_8974
from module_8975 import min_8975
from module_8976 import max_8976

def test_modulo_8973():
    assert modulo_8973(10, 3) == 1

def test_power_8974():
    assert power_8974(2, 8) == 256

def test_min_8975():
    assert min_8975(3, 7) == 3

def test_max_8976():
    assert max_8976(3, 7) == 7
