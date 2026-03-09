"""Tests for test module 1878 — covers src modules [7509, 7510, 7511, 7512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7509 import modulo_7509
from module_7510 import power_7510
from module_7511 import min_7511
from module_7512 import max_7512

def test_modulo_7509():
    assert modulo_7509(10, 3) == 1

def test_power_7510():
    assert power_7510(2, 8) == 256

def test_min_7511():
    assert min_7511(3, 7) == 3

def test_max_7512():
    assert max_7512(3, 7) == 7
