"""Tests for test module 1014 — covers src modules [4053, 4054, 4055, 4056]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4053 import modulo_4053
from module_4054 import power_4054
from module_4055 import min_4055
from module_4056 import max_4056

def test_modulo_4053():
    assert modulo_4053(10, 3) == 1

def test_power_4054():
    assert power_4054(2, 8) == 256

def test_min_4055():
    assert min_4055(3, 7) == 3

def test_max_4056():
    assert max_4056(3, 7) == 7
