"""Tests for test module 2182 — covers src modules [8725, 8726, 8727, 8728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8725 import modulo_8725
from module_8726 import power_8726
from module_8727 import min_8727
from module_8728 import max_8728

def test_modulo_8725():
    assert modulo_8725(10, 3) == 1

def test_power_8726():
    assert power_8726(2, 8) == 256

def test_min_8727():
    assert min_8727(3, 7) == 3

def test_max_8728():
    assert max_8728(3, 7) == 7
