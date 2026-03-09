"""Tests for test module 1078 — covers src modules [4309, 4310, 4311, 4312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4309 import modulo_4309
from module_4310 import power_4310
from module_4311 import min_4311
from module_4312 import max_4312

def test_modulo_4309():
    assert modulo_4309(10, 3) == 1

def test_power_4310():
    assert power_4310(2, 8) == 256

def test_min_4311():
    assert min_4311(3, 7) == 3

def test_max_4312():
    assert max_4312(3, 7) == 7
