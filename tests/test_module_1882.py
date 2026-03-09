"""Tests for test module 1882 — covers src modules [7525, 7526, 7527, 7528]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7525 import modulo_7525
from module_7526 import power_7526
from module_7527 import min_7527
from module_7528 import max_7528

def test_modulo_7525():
    assert modulo_7525(10, 3) == 1

def test_power_7526():
    assert power_7526(2, 8) == 256

def test_min_7527():
    assert min_7527(3, 7) == 3

def test_max_7528():
    assert max_7528(3, 7) == 7
