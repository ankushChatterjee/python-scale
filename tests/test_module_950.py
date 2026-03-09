"""Tests for test module 950 — covers src modules [3797, 3798, 3799, 3800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3797 import modulo_3797
from module_3798 import power_3798
from module_3799 import min_3799
from module_3800 import max_3800

def test_modulo_3797():
    assert modulo_3797(10, 3) == 1

def test_power_3798():
    assert power_3798(2, 8) == 256

def test_min_3799():
    assert min_3799(3, 7) == 3

def test_max_3800():
    assert max_3800(3, 7) == 7
