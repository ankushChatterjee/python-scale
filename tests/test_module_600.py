"""Tests for test module 600 — covers src modules [2397, 2398, 2399, 2400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2397 import modulo_2397
from module_2398 import power_2398
from module_2399 import min_2399
from module_2400 import max_2400

def test_modulo_2397():
    assert modulo_2397(10, 3) == 1

def test_power_2398():
    assert power_2398(2, 8) == 256

def test_min_2399():
    assert min_2399(3, 7) == 3

def test_max_2400():
    assert max_2400(3, 7) == 7
