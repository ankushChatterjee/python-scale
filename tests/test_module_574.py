"""Tests for test module 574 — covers src modules [2293, 2294, 2295, 2296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2293 import modulo_2293
from module_2294 import power_2294
from module_2295 import min_2295
from module_2296 import max_2296

def test_modulo_2293():
    assert modulo_2293(10, 3) == 1

def test_power_2294():
    assert power_2294(2, 8) == 256

def test_min_2295():
    assert min_2295(3, 7) == 3

def test_max_2296():
    assert max_2296(3, 7) == 7
