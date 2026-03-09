"""Tests for test module 1760 — covers src modules [7037, 7038, 7039, 7040]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7037 import modulo_7037
from module_7038 import power_7038
from module_7039 import min_7039
from module_7040 import max_7040

def test_modulo_7037():
    assert modulo_7037(10, 3) == 1

def test_power_7038():
    assert power_7038(2, 8) == 256

def test_min_7039():
    assert min_7039(3, 7) == 3

def test_max_7040():
    assert max_7040(3, 7) == 7
