"""Tests for test module 1432 — covers src modules [5725, 5726, 5727, 5728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5725 import modulo_5725
from module_5726 import power_5726
from module_5727 import min_5727
from module_5728 import max_5728

def test_modulo_5725():
    assert modulo_5725(10, 3) == 1

def test_power_5726():
    assert power_5726(2, 8) == 256

def test_min_5727():
    assert min_5727(3, 7) == 3

def test_max_5728():
    assert max_5728(3, 7) == 7
