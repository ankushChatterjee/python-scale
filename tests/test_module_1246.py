"""Tests for test module 1246 — covers src modules [4981, 4982, 4983, 4984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4981 import modulo_4981
from module_4982 import power_4982
from module_4983 import min_4983
from module_4984 import max_4984

def test_modulo_4981():
    assert modulo_4981(10, 3) == 1

def test_power_4982():
    assert power_4982(2, 8) == 256

def test_min_4983():
    assert min_4983(3, 7) == 3

def test_max_4984():
    assert max_4984(3, 7) == 7
