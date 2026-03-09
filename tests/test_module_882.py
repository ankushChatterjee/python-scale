"""Tests for test module 882 — covers src modules [3525, 3526, 3527, 3528]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3525 import modulo_3525
from module_3526 import power_3526
from module_3527 import min_3527
from module_3528 import max_3528

def test_modulo_3525():
    assert modulo_3525(10, 3) == 1

def test_power_3526():
    assert power_3526(2, 8) == 256

def test_min_3527():
    assert min_3527(3, 7) == 3

def test_max_3528():
    assert max_3528(3, 7) == 7
