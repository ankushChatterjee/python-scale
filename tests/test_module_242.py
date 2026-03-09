"""Tests for test module 242 — covers src modules [965, 966, 967, 968]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_965 import modulo_965
from module_966 import power_966
from module_967 import min_967
from module_968 import max_968

def test_modulo_965():
    assert modulo_965(10, 3) == 1

def test_power_966():
    assert power_966(2, 8) == 256

def test_min_967():
    assert min_967(3, 7) == 3

def test_max_968():
    assert max_968(3, 7) == 7
