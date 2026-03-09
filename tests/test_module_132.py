"""Tests for test module 132 — covers src modules [525, 526, 527, 528]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_525 import modulo_525
from module_526 import power_526
from module_527 import min_527
from module_528 import max_528

def test_modulo_525():
    assert modulo_525(10, 3) == 1

def test_power_526():
    assert power_526(2, 8) == 256

def test_min_527():
    assert min_527(3, 7) == 3

def test_max_528():
    assert max_528(3, 7) == 7
