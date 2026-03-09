"""Tests for test module 976 — covers src modules [3901, 3902, 3903, 3904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3901 import modulo_3901
from module_3902 import power_3902
from module_3903 import min_3903
from module_3904 import max_3904

def test_modulo_3901():
    assert modulo_3901(10, 3) == 1

def test_power_3902():
    assert power_3902(2, 8) == 256

def test_min_3903():
    assert min_3903(3, 7) == 3

def test_max_3904():
    assert max_3904(3, 7) == 7
