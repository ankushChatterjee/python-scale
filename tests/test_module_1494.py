"""Tests for test module 1494 — covers src modules [5973, 5974, 5975, 5976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5973 import modulo_5973
from module_5974 import power_5974
from module_5975 import min_5975
from module_5976 import max_5976

def test_modulo_5973():
    assert modulo_5973(10, 3) == 1

def test_power_5974():
    assert power_5974(2, 8) == 256

def test_min_5975():
    assert min_5975(3, 7) == 3

def test_max_5976():
    assert max_5976(3, 7) == 7
