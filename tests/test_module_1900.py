"""Tests for test module 1900 — covers src modules [7597, 7598, 7599, 7600]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7597 import modulo_7597
from module_7598 import power_7598
from module_7599 import min_7599
from module_7600 import max_7600

def test_modulo_7597():
    assert modulo_7597(10, 3) == 1

def test_power_7598():
    assert power_7598(2, 8) == 256

def test_min_7599():
    assert min_7599(3, 7) == 3

def test_max_7600():
    assert max_7600(3, 7) == 7
