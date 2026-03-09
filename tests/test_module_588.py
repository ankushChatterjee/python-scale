"""Tests for test module 588 — covers src modules [2349, 2350, 2351, 2352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2349 import modulo_2349
from module_2350 import power_2350
from module_2351 import min_2351
from module_2352 import max_2352

def test_modulo_2349():
    assert modulo_2349(10, 3) == 1

def test_power_2350():
    assert power_2350(2, 8) == 256

def test_min_2351():
    assert min_2351(3, 7) == 3

def test_max_2352():
    assert max_2352(3, 7) == 7
