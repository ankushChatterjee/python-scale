"""Tests for test module 1804 — covers src modules [7213, 7214, 7215, 7216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7213 import modulo_7213
from module_7214 import power_7214
from module_7215 import min_7215
from module_7216 import max_7216

def test_modulo_7213():
    assert modulo_7213(10, 3) == 1

def test_power_7214():
    assert power_7214(2, 8) == 256

def test_min_7215():
    assert min_7215(3, 7) == 3

def test_max_7216():
    assert max_7216(3, 7) == 7
