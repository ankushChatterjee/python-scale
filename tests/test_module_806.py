"""Tests for test module 806 — covers src modules [3221, 3222, 3223, 3224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3221 import modulo_3221
from module_3222 import power_3222
from module_3223 import min_3223
from module_3224 import max_3224

def test_modulo_3221():
    assert modulo_3221(10, 3) == 1

def test_power_3222():
    assert power_3222(2, 8) == 256

def test_min_3223():
    assert min_3223(3, 7) == 3

def test_max_3224():
    assert max_3224(3, 7) == 7
