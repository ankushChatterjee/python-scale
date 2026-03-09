"""Tests for test module 54 — covers src modules [213, 214, 215, 216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_213 import modulo_213
from module_214 import power_214
from module_215 import min_215
from module_216 import max_216

def test_modulo_213():
    assert modulo_213(10, 3) == 1

def test_power_214():
    assert power_214(2, 8) == 256

def test_min_215():
    assert min_215(3, 7) == 3

def test_max_216():
    assert max_216(3, 7) == 7
