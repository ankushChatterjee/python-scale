"""Tests for test module 1304 — covers src modules [5213, 5214, 5215, 5216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5213 import modulo_5213
from module_5214 import power_5214
from module_5215 import min_5215
from module_5216 import max_5216

def test_modulo_5213():
    assert modulo_5213(10, 3) == 1

def test_power_5214():
    assert power_5214(2, 8) == 256

def test_min_5215():
    assert min_5215(3, 7) == 3

def test_max_5216():
    assert max_5216(3, 7) == 7
