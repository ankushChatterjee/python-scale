"""Tests for test module 810 — covers src modules [3237, 3238, 3239, 3240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3237 import modulo_3237
from module_3238 import power_3238
from module_3239 import min_3239
from module_3240 import max_3240

def test_modulo_3237():
    assert modulo_3237(10, 3) == 1

def test_power_3238():
    assert power_3238(2, 8) == 256

def test_min_3239():
    assert min_3239(3, 7) == 3

def test_max_3240():
    assert max_3240(3, 7) == 7
