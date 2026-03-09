"""Tests for test module 2476 — covers src modules [9901, 9902, 9903, 9904]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9901 import modulo_9901
from module_9902 import power_9902
from module_9903 import min_9903
from module_9904 import max_9904

def test_modulo_9901():
    assert modulo_9901(10, 3) == 1

def test_power_9902():
    assert power_9902(2, 8) == 256

def test_min_9903():
    assert min_9903(3, 7) == 3

def test_max_9904():
    assert max_9904(3, 7) == 7
