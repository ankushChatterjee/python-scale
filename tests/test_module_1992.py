"""Tests for test module 1992 — covers src modules [7965, 7966, 7967, 7968]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7965 import modulo_7965
from module_7966 import power_7966
from module_7967 import min_7967
from module_7968 import max_7968

def test_modulo_7965():
    assert modulo_7965(10, 3) == 1

def test_power_7966():
    assert power_7966(2, 8) == 256

def test_min_7967():
    assert min_7967(3, 7) == 3

def test_max_7968():
    assert max_7968(3, 7) == 7
