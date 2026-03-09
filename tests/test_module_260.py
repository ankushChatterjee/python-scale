"""Tests for test module 260 — covers src modules [1037, 1038, 1039, 1040]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1037 import modulo_1037
from module_1038 import power_1038
from module_1039 import min_1039
from module_1040 import max_1040

def test_modulo_1037():
    assert modulo_1037(10, 3) == 1

def test_power_1038():
    assert power_1038(2, 8) == 256

def test_min_1039():
    assert min_1039(3, 7) == 3

def test_max_1040():
    assert max_1040(3, 7) == 7
