"""Tests for test module 2072 — covers src modules [8285, 8286, 8287, 8288]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8285 import modulo_8285
from module_8286 import power_8286
from module_8287 import min_8287
from module_8288 import max_8288

def test_modulo_8285():
    assert modulo_8285(10, 3) == 1

def test_power_8286():
    assert power_8286(2, 8) == 256

def test_min_8287():
    assert min_8287(3, 7) == 3

def test_max_8288():
    assert max_8288(3, 7) == 7
