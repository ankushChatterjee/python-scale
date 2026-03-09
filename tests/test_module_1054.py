"""Tests for test module 1054 — covers src modules [4213, 4214, 4215, 4216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4213 import modulo_4213
from module_4214 import power_4214
from module_4215 import min_4215
from module_4216 import max_4216

def test_modulo_4213():
    assert modulo_4213(10, 3) == 1

def test_power_4214():
    assert power_4214(2, 8) == 256

def test_min_4215():
    assert min_4215(3, 7) == 3

def test_max_4216():
    assert max_4216(3, 7) == 7
