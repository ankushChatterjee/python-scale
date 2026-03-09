"""Tests for test module 1182 — covers src modules [4725, 4726, 4727, 4728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4725 import modulo_4725
from module_4726 import power_4726
from module_4727 import min_4727
from module_4728 import max_4728

def test_modulo_4725():
    assert modulo_4725(10, 3) == 1

def test_power_4726():
    assert power_4726(2, 8) == 256

def test_min_4727():
    assert min_4727(3, 7) == 3

def test_max_4728():
    assert max_4728(3, 7) == 7
