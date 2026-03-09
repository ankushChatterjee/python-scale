"""Tests for test module 1060 — covers src modules [4237, 4238, 4239, 4240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4237 import modulo_4237
from module_4238 import power_4238
from module_4239 import min_4239
from module_4240 import max_4240

def test_modulo_4237():
    assert modulo_4237(10, 3) == 1

def test_power_4238():
    assert power_4238(2, 8) == 256

def test_min_4239():
    assert min_4239(3, 7) == 3

def test_max_4240():
    assert max_4240(3, 7) == 7
