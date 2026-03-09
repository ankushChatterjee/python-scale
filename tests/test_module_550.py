"""Tests for test module 550 — covers src modules [2197, 2198, 2199, 2200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2197 import modulo_2197
from module_2198 import power_2198
from module_2199 import min_2199
from module_2200 import max_2200

def test_modulo_2197():
    assert modulo_2197(10, 3) == 1

def test_power_2198():
    assert power_2198(2, 8) == 256

def test_min_2199():
    assert min_2199(3, 7) == 3

def test_max_2200():
    assert max_2200(3, 7) == 7
