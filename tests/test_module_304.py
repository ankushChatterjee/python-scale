"""Tests for test module 304 — covers src modules [1213, 1214, 1215, 1216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1213 import modulo_1213
from module_1214 import power_1214
from module_1215 import min_1215
from module_1216 import max_1216

def test_modulo_1213():
    assert modulo_1213(10, 3) == 1

def test_power_1214():
    assert power_1214(2, 8) == 256

def test_min_1215():
    assert min_1215(3, 7) == 3

def test_max_1216():
    assert max_1216(3, 7) == 7
