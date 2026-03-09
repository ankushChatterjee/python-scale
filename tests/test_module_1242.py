"""Tests for test module 1242 — covers src modules [4965, 4966, 4967, 4968]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4965 import modulo_4965
from module_4966 import power_4966
from module_4967 import min_4967
from module_4968 import max_4968

def test_modulo_4965():
    assert modulo_4965(10, 3) == 1

def test_power_4966():
    assert power_4966(2, 8) == 256

def test_min_4967():
    assert min_4967(3, 7) == 3

def test_max_4968():
    assert max_4968(3, 7) == 7
