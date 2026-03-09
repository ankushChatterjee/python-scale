"""Tests for test module 2150 — covers src modules [8597, 8598, 8599, 8600]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8597 import modulo_8597
from module_8598 import power_8598
from module_8599 import min_8599
from module_8600 import max_8600

def test_modulo_8597():
    assert modulo_8597(10, 3) == 1

def test_power_8598():
    assert power_8598(2, 8) == 256

def test_min_8599():
    assert min_8599(3, 7) == 3

def test_max_8600():
    assert max_8600(3, 7) == 7
