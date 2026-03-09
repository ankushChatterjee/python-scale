"""Tests for test module 400 — covers src modules [1597, 1598, 1599, 1600]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1597 import modulo_1597
from module_1598 import power_1598
from module_1599 import min_1599
from module_1600 import max_1600

def test_modulo_1597():
    assert modulo_1597(10, 3) == 1

def test_power_1598():
    assert power_1598(2, 8) == 256

def test_min_1599():
    assert min_1599(3, 7) == 3

def test_max_1600():
    assert max_1600(3, 7) == 7
