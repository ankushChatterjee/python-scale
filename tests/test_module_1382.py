"""Tests for test module 1382 — covers src modules [5525, 5526, 5527, 5528]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5525 import modulo_5525
from module_5526 import power_5526
from module_5527 import min_5527
from module_5528 import max_5528

def test_modulo_5525():
    assert modulo_5525(10, 3) == 1

def test_power_5526():
    assert power_5526(2, 8) == 256

def test_min_5527():
    assert min_5527(3, 7) == 3

def test_max_5528():
    assert max_5528(3, 7) == 7
