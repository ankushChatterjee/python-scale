"""Tests for test module 1010 — covers src modules [4037, 4038, 4039, 4040]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4037 import modulo_4037
from module_4038 import power_4038
from module_4039 import min_4039
from module_4040 import max_4040

def test_modulo_4037():
    assert modulo_4037(10, 3) == 1

def test_power_4038():
    assert power_4038(2, 8) == 256

def test_min_4039():
    assert min_4039(3, 7) == 3

def test_max_4040():
    assert max_4040(3, 7) == 7
