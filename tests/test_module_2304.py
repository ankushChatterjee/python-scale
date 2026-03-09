"""Tests for test module 2304 — covers src modules [9213, 9214, 9215, 9216]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9213 import modulo_9213
from module_9214 import power_9214
from module_9215 import min_9215
from module_9216 import max_9216

def test_modulo_9213():
    assert modulo_9213(10, 3) == 1

def test_power_9214():
    assert power_9214(2, 8) == 256

def test_min_9215():
    assert min_9215(3, 7) == 3

def test_max_9216():
    assert max_9216(3, 7) == 7
