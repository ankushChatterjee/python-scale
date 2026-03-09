"""Tests for test module 2338 — covers src modules [9349, 9350, 9351, 9352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9349 import modulo_9349
from module_9350 import power_9350
from module_9351 import min_9351
from module_9352 import max_9352

def test_modulo_9349():
    assert modulo_9349(10, 3) == 1

def test_power_9350():
    assert power_9350(2, 8) == 256

def test_min_9351():
    assert min_9351(3, 7) == 3

def test_max_9352():
    assert max_9352(3, 7) == 7
