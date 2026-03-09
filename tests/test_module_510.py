"""Tests for test module 510 — covers src modules [2037, 2038, 2039, 2040]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2037 import modulo_2037
from module_2038 import power_2038
from module_2039 import min_2039
from module_2040 import max_2040

def test_modulo_2037():
    assert modulo_2037(10, 3) == 1

def test_power_2038():
    assert power_2038(2, 8) == 256

def test_min_2039():
    assert min_2039(3, 7) == 3

def test_max_2040():
    assert max_2040(3, 7) == 7
