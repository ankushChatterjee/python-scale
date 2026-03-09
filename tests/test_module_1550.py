"""Tests for test module 1550 — covers src modules [6197, 6198, 6199, 6200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6197 import modulo_6197
from module_6198 import power_6198
from module_6199 import min_6199
from module_6200 import max_6200

def test_modulo_6197():
    assert modulo_6197(10, 3) == 1

def test_power_6198():
    assert power_6198(2, 8) == 256

def test_min_6199():
    assert min_6199(3, 7) == 3

def test_max_6200():
    assert max_6200(3, 7) == 7
