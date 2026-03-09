"""Tests for test module 900 — covers src modules [3597, 3598, 3599, 3600]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3597 import modulo_3597
from module_3598 import power_3598
from module_3599 import min_3599
from module_3600 import max_3600

def test_modulo_3597():
    assert modulo_3597(10, 3) == 1

def test_power_3598():
    assert power_3598(2, 8) == 256

def test_min_3599():
    assert min_3599(3, 7) == 3

def test_max_3600():
    assert max_3600(3, 7) == 7
