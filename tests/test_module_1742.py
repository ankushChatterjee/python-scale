"""Tests for test module 1742 — covers src modules [6965, 6966, 6967, 6968]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6965 import modulo_6965
from module_6966 import power_6966
from module_6967 import min_6967
from module_6968 import max_6968

def test_modulo_6965():
    assert modulo_6965(10, 3) == 1

def test_power_6966():
    assert power_6966(2, 8) == 256

def test_min_6967():
    assert min_6967(3, 7) == 3

def test_max_6968():
    assert max_6968(3, 7) == 7
