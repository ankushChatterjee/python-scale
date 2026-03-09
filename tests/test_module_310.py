"""Tests for test module 310 — covers src modules [1237, 1238, 1239, 1240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1237 import modulo_1237
from module_1238 import power_1238
from module_1239 import min_1239
from module_1240 import max_1240

def test_modulo_1237():
    assert modulo_1237(10, 3) == 1

def test_power_1238():
    assert power_1238(2, 8) == 256

def test_min_1239():
    assert min_1239(3, 7) == 3

def test_max_1240():
    assert max_1240(3, 7) == 7
