"""Tests for test module 824 — covers src modules [3293, 3294, 3295, 3296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3293 import modulo_3293
from module_3294 import power_3294
from module_3295 import min_3295
from module_3296 import max_3296

def test_modulo_3293():
    assert modulo_3293(10, 3) == 1

def test_power_3294():
    assert power_3294(2, 8) == 256

def test_min_3295():
    assert min_3295(3, 7) == 3

def test_max_3296():
    assert max_3296(3, 7) == 7
