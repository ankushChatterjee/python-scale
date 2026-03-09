"""Tests for test module 2290 — covers src modules [9157, 9158, 9159, 9160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9157 import modulo_9157
from module_9158 import power_9158
from module_9159 import min_9159
from module_9160 import max_9160

def test_modulo_9157():
    assert modulo_9157(10, 3) == 1

def test_power_9158():
    assert power_9158(2, 8) == 256

def test_min_9159():
    assert min_9159(3, 7) == 3

def test_max_9160():
    assert max_9160(3, 7) == 7
