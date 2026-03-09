"""Tests for test module 432 — covers src modules [1725, 1726, 1727, 1728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1725 import modulo_1725
from module_1726 import power_1726
from module_1727 import min_1727
from module_1728 import max_1728

def test_modulo_1725():
    assert modulo_1725(10, 3) == 1

def test_power_1726():
    assert power_1726(2, 8) == 256

def test_min_1727():
    assert min_1727(3, 7) == 3

def test_max_1728():
    assert max_1728(3, 7) == 7
