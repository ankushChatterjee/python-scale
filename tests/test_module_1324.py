"""Tests for test module 1324 — covers src modules [5293, 5294, 5295, 5296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5293 import modulo_5293
from module_5294 import power_5294
from module_5295 import min_5295
from module_5296 import max_5296

def test_modulo_5293():
    assert modulo_5293(10, 3) == 1

def test_power_5294():
    assert power_5294(2, 8) == 256

def test_min_5295():
    assert min_5295(3, 7) == 3

def test_max_5296():
    assert max_5296(3, 7) == 7
