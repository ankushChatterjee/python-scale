"""Tests for test module 1300 — covers src modules [5197, 5198, 5199, 5200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5197 import modulo_5197
from module_5198 import power_5198
from module_5199 import min_5199
from module_5200 import max_5200

def test_modulo_5197():
    assert modulo_5197(10, 3) == 1

def test_power_5198():
    assert power_5198(2, 8) == 256

def test_min_5199():
    assert min_5199(3, 7) == 3

def test_max_5200():
    assert max_5200(3, 7) == 7
