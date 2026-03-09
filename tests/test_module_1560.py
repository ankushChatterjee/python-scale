"""Tests for test module 1560 — covers src modules [6237, 6238, 6239, 6240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6237 import modulo_6237
from module_6238 import power_6238
from module_6239 import min_6239
from module_6240 import max_6240

def test_modulo_6237():
    assert modulo_6237(10, 3) == 1

def test_power_6238():
    assert power_6238(2, 8) == 256

def test_min_6239():
    assert min_6239(3, 7) == 3

def test_max_6240():
    assert max_6240(3, 7) == 7
