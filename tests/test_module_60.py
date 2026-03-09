"""Tests for test module 60 — covers src modules [237, 238, 239, 240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_237 import modulo_237
from module_238 import power_238
from module_239 import min_239
from module_240 import max_240

def test_modulo_237():
    assert modulo_237(10, 3) == 1

def test_power_238():
    assert power_238(2, 8) == 256

def test_min_239():
    assert min_239(3, 7) == 3

def test_max_240():
    assert max_240(3, 7) == 7
