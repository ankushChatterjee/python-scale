"""Tests for test module 1810 — covers src modules [7237, 7238, 7239, 7240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7237 import modulo_7237
from module_7238 import power_7238
from module_7239 import min_7239
from module_7240 import max_7240

def test_modulo_7237():
    assert modulo_7237(10, 3) == 1

def test_power_7238():
    assert power_7238(2, 8) == 256

def test_min_7239():
    assert min_7239(3, 7) == 3

def test_max_7240():
    assert max_7240(3, 7) == 7
