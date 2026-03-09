"""Tests for test module 1310 — covers src modules [5237, 5238, 5239, 5240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5237 import modulo_5237
from module_5238 import power_5238
from module_5239 import min_5239
from module_5240 import max_5240

def test_modulo_5237():
    assert modulo_5237(10, 3) == 1

def test_power_5238():
    assert power_5238(2, 8) == 256

def test_min_5239():
    assert min_5239(3, 7) == 3

def test_max_5240():
    assert max_5240(3, 7) == 7
