"""Tests for test module 1260 — covers src modules [5037, 5038, 5039, 5040]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5037 import modulo_5037
from module_5038 import power_5038
from module_5039 import min_5039
from module_5040 import max_5040

def test_modulo_5037():
    assert modulo_5037(10, 3) == 1

def test_power_5038():
    assert power_5038(2, 8) == 256

def test_min_5039():
    assert min_5039(3, 7) == 3

def test_max_5040():
    assert max_5040(3, 7) == 7
