"""Tests for test module 2310 — covers src modules [9237, 9238, 9239, 9240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9237 import modulo_9237
from module_9238 import power_9238
from module_9239 import min_9239
from module_9240 import max_9240

def test_modulo_9237():
    assert modulo_9237(10, 3) == 1

def test_power_9238():
    assert power_9238(2, 8) == 256

def test_min_9239():
    assert min_9239(3, 7) == 3

def test_max_9240():
    assert max_9240(3, 7) == 7
