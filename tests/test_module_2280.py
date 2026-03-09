"""Tests for test module 2280 — covers src modules [9117, 9118, 9119, 9120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9117 import modulo_9117
from module_9118 import power_9118
from module_9119 import min_9119
from module_9120 import max_9120

def test_modulo_9117():
    assert modulo_9117(10, 3) == 1

def test_power_9118():
    assert power_9118(2, 8) == 256

def test_min_9119():
    assert min_9119(3, 7) == 3

def test_max_9120():
    assert max_9120(3, 7) == 7
