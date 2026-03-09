"""Tests for test module 800 — covers src modules [3197, 3198, 3199, 3200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3197 import modulo_3197
from module_3198 import power_3198
from module_3199 import min_3199
from module_3200 import max_3200

def test_modulo_3197():
    assert modulo_3197(10, 3) == 1

def test_power_3198():
    assert power_3198(2, 8) == 256

def test_min_3199():
    assert min_3199(3, 7) == 3

def test_max_3200():
    assert max_3200(3, 7) == 7
