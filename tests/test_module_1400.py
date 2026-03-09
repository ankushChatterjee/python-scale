"""Tests for test module 1400 — covers src modules [5597, 5598, 5599, 5600]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5597 import modulo_5597
from module_5598 import power_5598
from module_5599 import min_5599
from module_5600 import max_5600

def test_modulo_5597():
    assert modulo_5597(10, 3) == 1

def test_power_5598():
    assert power_5598(2, 8) == 256

def test_min_5599():
    assert min_5599(3, 7) == 3

def test_max_5600():
    assert max_5600(3, 7) == 7
