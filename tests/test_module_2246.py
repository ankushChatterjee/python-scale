"""Tests for test module 2246 — covers src modules [8981, 8982, 8983, 8984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8981 import modulo_8981
from module_8982 import power_8982
from module_8983 import min_8983
from module_8984 import max_8984

def test_modulo_8981():
    assert modulo_8981(10, 3) == 1

def test_power_8982():
    assert power_8982(2, 8) == 256

def test_min_8983():
    assert min_8983(3, 7) == 3

def test_max_8984():
    assert max_8984(3, 7) == 7
