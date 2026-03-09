"""Tests for test module 2074 — covers src modules [8293, 8294, 8295, 8296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8293 import modulo_8293
from module_8294 import power_8294
from module_8295 import min_8295
from module_8296 import max_8296

def test_modulo_8293():
    assert modulo_8293(10, 3) == 1

def test_power_8294():
    assert power_8294(2, 8) == 256

def test_min_8295():
    assert min_8295(3, 7) == 3

def test_max_8296():
    assert max_8296(3, 7) == 7
