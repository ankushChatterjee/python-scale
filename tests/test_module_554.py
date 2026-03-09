"""Tests for test module 554 — covers src modules [2213, 2214, 2215, 2216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2213 import modulo_2213
from module_2214 import power_2214
from module_2215 import min_2215
from module_2216 import max_2216

def test_modulo_2213():
    assert modulo_2213(10, 3) == 1

def test_power_2214():
    assert power_2214(2, 8) == 256

def test_min_2215():
    assert min_2215(3, 7) == 3

def test_max_2216():
    assert max_2216(3, 7) == 7
