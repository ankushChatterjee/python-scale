"""Tests for test module 2054 — covers src modules [8213, 8214, 8215, 8216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8213 import modulo_8213
from module_8214 import power_8214
from module_8215 import min_8215
from module_8216 import max_8216

def test_modulo_8213():
    assert modulo_8213(10, 3) == 1

def test_power_8214():
    assert power_8214(2, 8) == 256

def test_min_8215():
    assert min_8215(3, 7) == 3

def test_max_8216():
    assert max_8216(3, 7) == 7
