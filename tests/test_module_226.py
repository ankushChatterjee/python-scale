"""Tests for test module 226 — covers src modules [901, 902, 903, 904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_901 import modulo_901
from module_902 import power_902
from module_903 import min_903
from module_904 import max_904

def test_modulo_901():
    assert modulo_901(10, 3) == 1

def test_power_902():
    assert power_902(2, 8) == 256

def test_min_903():
    assert min_903(3, 7) == 3

def test_max_904():
    assert max_904(3, 7) == 7
