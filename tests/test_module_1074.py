"""Tests for test module 1074 — covers src modules [4293, 4294, 4295, 4296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4293 import modulo_4293
from module_4294 import power_4294
from module_4295 import min_4295
from module_4296 import max_4296

def test_modulo_4293():
    assert modulo_4293(10, 3) == 1

def test_power_4294():
    assert power_4294(2, 8) == 256

def test_min_4295():
    assert min_4295(3, 7) == 3

def test_max_4296():
    assert max_4296(3, 7) == 7
