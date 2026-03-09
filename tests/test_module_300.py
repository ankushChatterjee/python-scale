"""Tests for test module 300 — covers src modules [1197, 1198, 1199, 1200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1197 import modulo_1197
from module_1198 import power_1198
from module_1199 import min_1199
from module_1200 import max_1200

def test_modulo_1197():
    assert modulo_1197(10, 3) == 1

def test_power_1198():
    assert power_1198(2, 8) == 256

def test_min_1199():
    assert min_1199(3, 7) == 3

def test_max_1200():
    assert max_1200(3, 7) == 7
