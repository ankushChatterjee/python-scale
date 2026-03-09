"""Tests for test module 1574 — covers src modules [6293, 6294, 6295, 6296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6293 import modulo_6293
from module_6294 import power_6294
from module_6295 import min_6295
from module_6296 import max_6296

def test_modulo_6293():
    assert modulo_6293(10, 3) == 1

def test_power_6294():
    assert power_6294(2, 8) == 256

def test_min_6295():
    assert min_6295(3, 7) == 3

def test_max_6296():
    assert max_6296(3, 7) == 7
