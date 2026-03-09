"""Tests for test module 1226 — covers src modules [4901, 4902, 4903, 4904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4901 import modulo_4901
from module_4902 import power_4902
from module_4903 import min_4903
from module_4904 import max_4904

def test_modulo_4901():
    assert modulo_4901(10, 3) == 1

def test_power_4902():
    assert power_4902(2, 8) == 256

def test_min_4903():
    assert min_4903(3, 7) == 3

def test_max_4904():
    assert max_4904(3, 7) == 7
