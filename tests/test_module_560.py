"""Tests for test module 560 — covers src modules [2237, 2238, 2239, 2240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2237 import modulo_2237
from module_2238 import power_2238
from module_2239 import min_2239
from module_2240 import max_2240

def test_modulo_2237():
    assert modulo_2237(10, 3) == 1

def test_power_2238():
    assert power_2238(2, 8) == 256

def test_min_2239():
    assert min_2239(3, 7) == 3

def test_max_2240():
    assert max_2240(3, 7) == 7
