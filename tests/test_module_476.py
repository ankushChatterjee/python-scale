"""Tests for test module 476 — covers src modules [1901, 1902, 1903, 1904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1901 import modulo_1901
from module_1902 import power_1902
from module_1903 import min_1903
from module_1904 import max_1904

def test_modulo_1901():
    assert modulo_1901(10, 3) == 1

def test_power_1902():
    assert power_1902(2, 8) == 256

def test_min_1903():
    assert min_1903(3, 7) == 3

def test_max_1904():
    assert max_1904(3, 7) == 7
