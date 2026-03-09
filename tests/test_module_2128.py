"""Tests for test module 2128 — covers src modules [8509, 8510, 8511, 8512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8509 import modulo_8509
from module_8510 import power_8510
from module_8511 import min_8511
from module_8512 import max_8512

def test_modulo_8509():
    assert modulo_8509(10, 3) == 1

def test_power_8510():
    assert power_8510(2, 8) == 256

def test_min_8511():
    assert min_8511(3, 7) == 3

def test_max_8512():
    assert max_8512(3, 7) == 7
