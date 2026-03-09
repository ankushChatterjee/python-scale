"""Tests for test module 150 — covers src modules [597, 598, 599, 600]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_597 import modulo_597
from module_598 import power_598
from module_599 import min_599
from module_600 import max_600

def test_modulo_597():
    assert modulo_597(10, 3) == 1

def test_power_598():
    assert power_598(2, 8) == 256

def test_min_599():
    assert min_599(3, 7) == 3

def test_max_600():
    assert max_600(3, 7) == 7
