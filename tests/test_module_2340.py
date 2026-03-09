"""Tests for test module 2340 — covers src modules [9357, 9358, 9359, 9360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9357 import modulo_9357
from module_9358 import power_9358
from module_9359 import min_9359
from module_9360 import max_9360

def test_modulo_9357():
    assert modulo_9357(10, 3) == 1

def test_power_9358():
    assert power_9358(2, 8) == 256

def test_min_9359():
    assert min_9359(3, 7) == 3

def test_max_9360():
    assert max_9360(3, 7) == 7
