"""Tests for test module 1244 — covers src modules [4973, 4974, 4975, 4976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4973 import modulo_4973
from module_4974 import power_4974
from module_4975 import min_4975
from module_4976 import max_4976

def test_modulo_4973():
    assert modulo_4973(10, 3) == 1

def test_power_4974():
    assert power_4974(2, 8) == 256

def test_min_4975():
    assert min_4975(3, 7) == 3

def test_max_4976():
    assert max_4976(3, 7) == 7
