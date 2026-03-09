"""Tests for test module 1682 — covers src modules [6725, 6726, 6727, 6728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6725 import modulo_6725
from module_6726 import power_6726
from module_6727 import min_6727
from module_6728 import max_6728

def test_modulo_6725():
    assert modulo_6725(10, 3) == 1

def test_power_6726():
    assert power_6726(2, 8) == 256

def test_min_6727():
    assert min_6727(3, 7) == 3

def test_max_6728():
    assert max_6728(3, 7) == 7
