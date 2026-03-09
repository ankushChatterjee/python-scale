"""Tests for test module 182 — covers src modules [725, 726, 727, 728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_725 import modulo_725
from module_726 import power_726
from module_727 import min_727
from module_728 import max_728

def test_modulo_725():
    assert modulo_725(10, 3) == 1

def test_power_726():
    assert power_726(2, 8) == 256

def test_min_727():
    assert min_727(3, 7) == 3

def test_max_728():
    assert max_728(3, 7) == 7
