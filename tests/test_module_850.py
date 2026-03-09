"""Tests for test module 850 — covers src modules [3397, 3398, 3399, 3400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3397 import modulo_3397
from module_3398 import power_3398
from module_3399 import min_3399
from module_3400 import max_3400

def test_modulo_3397():
    assert modulo_3397(10, 3) == 1

def test_power_3398():
    assert power_3398(2, 8) == 256

def test_min_3399():
    assert min_3399(3, 7) == 3

def test_max_3400():
    assert max_3400(3, 7) == 7
