"""Tests for test module 760 — covers src modules [3037, 3038, 3039, 3040]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3037 import modulo_3037
from module_3038 import power_3038
from module_3039 import min_3039
from module_3040 import max_3040

def test_modulo_3037():
    assert modulo_3037(10, 3) == 1

def test_power_3038():
    assert power_3038(2, 8) == 256

def test_min_3039():
    assert min_3039(3, 7) == 3

def test_max_3040():
    assert max_3040(3, 7) == 7
