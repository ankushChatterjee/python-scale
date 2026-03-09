"""Tests for test module 814 — covers src modules [3253, 3254, 3255, 3256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3253 import modulo_3253
from module_3254 import power_3254
from module_3255 import min_3255
from module_3256 import max_3256

def test_modulo_3253():
    assert modulo_3253(10, 3) == 1

def test_power_3254():
    assert power_3254(2, 8) == 256

def test_min_3255():
    assert min_3255(3, 7) == 3

def test_max_3256():
    assert max_3256(3, 7) == 7
