"""Tests for test module 1800 — covers src modules [7197, 7198, 7199, 7200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7197 import modulo_7197
from module_7198 import power_7198
from module_7199 import min_7199
from module_7200 import max_7200

def test_modulo_7197():
    assert modulo_7197(10, 3) == 1

def test_power_7198():
    assert power_7198(2, 8) == 256

def test_min_7199():
    assert min_7199(3, 7) == 3

def test_max_7200():
    assert max_7200(3, 7) == 7
