"""Tests for test module 726 — covers src modules [2901, 2902, 2903, 2904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2901 import modulo_2901
from module_2902 import power_2902
from module_2903 import min_2903
from module_2904 import max_2904

def test_modulo_2901():
    assert modulo_2901(10, 3) == 1

def test_power_2902():
    assert power_2902(2, 8) == 256

def test_min_2903():
    assert min_2903(3, 7) == 3

def test_max_2904():
    assert max_2904(3, 7) == 7
