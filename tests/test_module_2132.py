"""Tests for test module 2132 — covers src modules [8525, 8526, 8527, 8528]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8525 import modulo_8525
from module_8526 import power_8526
from module_8527 import min_8527
from module_8528 import max_8528

def test_modulo_8525():
    assert modulo_8525(10, 3) == 1

def test_power_8526():
    assert power_8526(2, 8) == 256

def test_min_8527():
    assert min_8527(3, 7) == 3

def test_max_8528():
    assert max_8528(3, 7) == 7
