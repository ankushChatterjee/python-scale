"""Tests for test module 994 — covers src modules [3973, 3974, 3975, 3976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3973 import modulo_3973
from module_3974 import power_3974
from module_3975 import min_3975
from module_3976 import max_3976

def test_modulo_3973():
    assert modulo_3973(10, 3) == 1

def test_power_3974():
    assert power_3974(2, 8) == 256

def test_min_3975():
    assert min_3975(3, 7) == 3

def test_max_3976():
    assert max_3976(3, 7) == 7
