"""Tests for test module 1726 — covers src modules [6901, 6902, 6903, 6904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6901 import modulo_6901
from module_6902 import power_6902
from module_6903 import min_6903
from module_6904 import max_6904

def test_modulo_6901():
    assert modulo_6901(10, 3) == 1

def test_power_6902():
    assert power_6902(2, 8) == 256

def test_min_6903():
    assert min_6903(3, 7) == 3

def test_max_6904():
    assert max_6904(3, 7) == 7
