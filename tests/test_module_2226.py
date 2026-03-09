"""Tests for test module 2226 — covers src modules [8901, 8902, 8903, 8904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8901 import modulo_8901
from module_8902 import power_8902
from module_8903 import min_8903
from module_8904 import max_8904

def test_modulo_8901():
    assert modulo_8901(10, 3) == 1

def test_power_8902():
    assert power_8902(2, 8) == 256

def test_min_8903():
    assert min_8903(3, 7) == 3

def test_max_8904():
    assert max_8904(3, 7) == 7
