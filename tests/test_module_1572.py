"""Tests for test module 1572 — covers src modules [6285, 6286, 6287, 6288]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6285 import modulo_6285
from module_6286 import power_6286
from module_6287 import min_6287
from module_6288 import max_6288

def test_modulo_6285():
    assert modulo_6285(10, 3) == 1

def test_power_6286():
    assert power_6286(2, 8) == 256

def test_min_6287():
    assert min_6287(3, 7) == 3

def test_max_6288():
    assert max_6288(3, 7) == 7
