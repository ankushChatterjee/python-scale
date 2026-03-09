"""Tests for test module 1824 — covers src modules [7293, 7294, 7295, 7296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7293 import modulo_7293
from module_7294 import power_7294
from module_7295 import min_7295
from module_7296 import max_7296

def test_modulo_7293():
    assert modulo_7293(10, 3) == 1

def test_power_7294():
    assert power_7294(2, 8) == 256

def test_min_7295():
    assert min_7295(3, 7) == 3

def test_max_7296():
    assert max_7296(3, 7) == 7
