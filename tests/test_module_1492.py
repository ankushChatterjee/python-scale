"""Tests for test module 1492 — covers src modules [5965, 5966, 5967, 5968]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5965 import modulo_5965
from module_5966 import power_5966
from module_5967 import min_5967
from module_5968 import max_5968

def test_modulo_5965():
    assert modulo_5965(10, 3) == 1

def test_power_5966():
    assert power_5966(2, 8) == 256

def test_min_5967():
    assert min_5967(3, 7) == 3

def test_max_5968():
    assert max_5968(3, 7) == 7
