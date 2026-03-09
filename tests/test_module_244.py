"""Tests for test module 244 — covers src modules [973, 974, 975, 976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_973 import modulo_973
from module_974 import power_974
from module_975 import min_975
from module_976 import max_976

def test_modulo_973():
    assert modulo_973(10, 3) == 1

def test_power_974():
    assert power_974(2, 8) == 256

def test_min_975():
    assert min_975(3, 7) == 3

def test_max_976():
    assert max_976(3, 7) == 7
