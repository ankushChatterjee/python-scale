"""Tests for test module 632 — covers src modules [2525, 2526, 2527, 2528]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2525 import modulo_2525
from module_2526 import power_2526
from module_2527 import min_2527
from module_2528 import max_2528

def test_modulo_2525():
    assert modulo_2525(10, 3) == 1

def test_power_2526():
    assert power_2526(2, 8) == 256

def test_min_2527():
    assert min_2527(3, 7) == 3

def test_max_2528():
    assert max_2528(3, 7) == 7
