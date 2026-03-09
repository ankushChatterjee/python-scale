"""Tests for test module 1476 — covers src modules [5901, 5902, 5903, 5904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5901 import modulo_5901
from module_5902 import power_5902
from module_5903 import min_5903
from module_5904 import max_5904

def test_modulo_5901():
    assert modulo_5901(10, 3) == 1

def test_power_5902():
    assert power_5902(2, 8) == 256

def test_min_5903():
    assert min_5903(3, 7) == 3

def test_max_5904():
    assert max_5904(3, 7) == 7
