"""Tests for test module 804 — covers src modules [3213, 3214, 3215, 3216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3213 import modulo_3213
from module_3214 import power_3214
from module_3215 import min_3215
from module_3216 import max_3216

def test_modulo_3213():
    assert modulo_3213(10, 3) == 1

def test_power_3214():
    assert power_3214(2, 8) == 256

def test_min_3215():
    assert min_3215(3, 7) == 3

def test_max_3216():
    assert max_3216(3, 7) == 7
