"""Tests for test module 996 — covers src modules [3981, 3982, 3983, 3984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3981 import modulo_3981
from module_3982 import power_3982
from module_3983 import min_3983
from module_3984 import max_3984

def test_modulo_3981():
    assert modulo_3981(10, 3) == 1

def test_power_3982():
    assert power_3982(2, 8) == 256

def test_min_3983():
    assert min_3983(3, 7) == 3

def test_max_3984():
    assert max_3984(3, 7) == 7
