"""Tests for test module 2242 — covers src modules [8965, 8966, 8967, 8968]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8965 import modulo_8965
from module_8966 import power_8966
from module_8967 import min_8967
from module_8968 import max_8968

def test_modulo_8965():
    assert modulo_8965(10, 3) == 1

def test_power_8966():
    assert power_8966(2, 8) == 256

def test_min_8967():
    assert min_8967(3, 7) == 3

def test_max_8968():
    assert max_8968(3, 7) == 7
