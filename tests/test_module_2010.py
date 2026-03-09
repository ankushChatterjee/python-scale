"""Tests for test module 2010 — covers src modules [8037, 8038, 8039, 8040]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8037 import modulo_8037
from module_8038 import power_8038
from module_8039 import min_8039
from module_8040 import max_8040

def test_modulo_8037():
    assert modulo_8037(10, 3) == 1

def test_power_8038():
    assert power_8038(2, 8) == 256

def test_min_8039():
    assert min_8039(3, 7) == 3

def test_max_8040():
    assert max_8040(3, 7) == 7
