"""Tests for test module 572 — covers src modules [2285, 2286, 2287, 2288]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2285 import modulo_2285
from module_2286 import power_2286
from module_2287 import min_2287
from module_2288 import max_2288

def test_modulo_2285():
    assert modulo_2285(10, 3) == 1

def test_power_2286():
    assert power_2286(2, 8) == 256

def test_min_2287():
    assert min_2287(3, 7) == 3

def test_max_2288():
    assert max_2288(3, 7) == 7
