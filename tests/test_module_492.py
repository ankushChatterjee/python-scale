"""Tests for test module 492 — covers src modules [1965, 1966, 1967, 1968]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1965 import modulo_1965
from module_1966 import power_1966
from module_1967 import min_1967
from module_1968 import max_1968

def test_modulo_1965():
    assert modulo_1965(10, 3) == 1

def test_power_1966():
    assert power_1966(2, 8) == 256

def test_min_1967():
    assert min_1967(3, 7) == 3

def test_max_1968():
    assert max_1968(3, 7) == 7
