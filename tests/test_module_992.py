"""Tests for test module 992 — covers src modules [3965, 3966, 3967, 3968]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3965 import modulo_3965
from module_3966 import power_3966
from module_3967 import min_3967
from module_3968 import max_3968

def test_modulo_3965():
    assert modulo_3965(10, 3) == 1

def test_power_3966():
    assert power_3966(2, 8) == 256

def test_min_3967():
    assert min_3967(3, 7) == 3

def test_max_3968():
    assert max_3968(3, 7) == 7
