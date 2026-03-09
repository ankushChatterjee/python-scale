"""Tests for test module 50 — covers src modules [197, 198, 199, 200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_197 import modulo_197
from module_198 import power_198
from module_199 import min_199
from module_200 import max_200

def test_modulo_197():
    assert modulo_197(10, 3) == 1

def test_power_198():
    assert power_198(2, 8) == 256

def test_min_199():
    assert min_199(3, 7) == 3

def test_max_200():
    assert max_200(3, 7) == 7
