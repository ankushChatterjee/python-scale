"""Tests for test module 1820 — covers src modules [7277, 7278, 7279, 7280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7277 import modulo_7277
from module_7278 import power_7278
from module_7279 import min_7279
from module_7280 import max_7280

def test_modulo_7277():
    assert modulo_7277(10, 3) == 1

def test_power_7278():
    assert power_7278(2, 8) == 256

def test_min_7279():
    assert min_7279(3, 7) == 3

def test_max_7280():
    assert max_7280(3, 7) == 7
