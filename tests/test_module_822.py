"""Tests for test module 822 — covers src modules [3285, 3286, 3287, 3288]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3285 import modulo_3285
from module_3286 import power_3286
from module_3287 import min_3287
from module_3288 import max_3288

def test_modulo_3285():
    assert modulo_3285(10, 3) == 1

def test_power_3286():
    assert power_3286(2, 8) == 256

def test_min_3287():
    assert min_3287(3, 7) == 3

def test_max_3288():
    assert max_3288(3, 7) == 7
