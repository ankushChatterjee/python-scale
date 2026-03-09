"""Tests for test module 932 — covers src modules [3725, 3726, 3727, 3728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3725 import modulo_3725
from module_3726 import power_3726
from module_3727 import min_3727
from module_3728 import max_3728

def test_modulo_3725():
    assert modulo_3725(10, 3) == 1

def test_power_3726():
    assert power_3726(2, 8) == 256

def test_min_3727():
    assert min_3727(3, 7) == 3

def test_max_3728():
    assert max_3728(3, 7) == 7
