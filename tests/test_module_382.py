"""Tests for test module 382 — covers src modules [1525, 1526, 1527, 1528]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1525 import modulo_1525
from module_1526 import power_1526
from module_1527 import min_1527
from module_1528 import max_1528

def test_modulo_1525():
    assert modulo_1525(10, 3) == 1

def test_power_1526():
    assert power_1526(2, 8) == 256

def test_min_1527():
    assert min_1527(3, 7) == 3

def test_max_1528():
    assert max_1528(3, 7) == 7
