"""Tests for test module 1976 — covers src modules [7901, 7902, 7903, 7904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7901 import modulo_7901
from module_7902 import power_7902
from module_7903 import min_7903
from module_7904 import max_7904

def test_modulo_7901():
    assert modulo_7901(10, 3) == 1

def test_power_7902():
    assert power_7902(2, 8) == 256

def test_min_7903():
    assert min_7903(3, 7) == 3

def test_max_7904():
    assert max_7904(3, 7) == 7
