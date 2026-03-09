"""Tests for test module 1744 — covers src modules [6973, 6974, 6975, 6976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6973 import modulo_6973
from module_6974 import power_6974
from module_6975 import min_6975
from module_6976 import max_6976

def test_modulo_6973():
    assert modulo_6973(10, 3) == 1

def test_power_6974():
    assert power_6974(2, 8) == 256

def test_min_6975():
    assert min_6975(3, 7) == 3

def test_max_6976():
    assert max_6976(3, 7) == 7
