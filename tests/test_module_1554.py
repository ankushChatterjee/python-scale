"""Tests for test module 1554 — covers src modules [6213, 6214, 6215, 6216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6213 import modulo_6213
from module_6214 import power_6214
from module_6215 import min_6215
from module_6216 import max_6216

def test_modulo_6213():
    assert modulo_6213(10, 3) == 1

def test_power_6214():
    assert power_6214(2, 8) == 256

def test_min_6215():
    assert min_6215(3, 7) == 3

def test_max_6216():
    assert max_6216(3, 7) == 7
