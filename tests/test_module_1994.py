"""Tests for test module 1994 — covers src modules [7973, 7974, 7975, 7976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7973 import modulo_7973
from module_7974 import power_7974
from module_7975 import min_7975
from module_7976 import max_7976

def test_modulo_7973():
    assert modulo_7973(10, 3) == 1

def test_power_7974():
    assert power_7974(2, 8) == 256

def test_min_7975():
    assert min_7975(3, 7) == 3

def test_max_7976():
    assert max_7976(3, 7) == 7
