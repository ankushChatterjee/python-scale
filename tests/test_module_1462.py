"""Tests for test module 1462 — covers src modules [5845, 5846, 5847, 5848]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5845 import modulo_5845
from module_5846 import power_5846
from module_5847 import min_5847
from module_5848 import max_5848

def test_modulo_5845():
    assert modulo_5845(10, 3) == 1

def test_power_5846():
    assert power_5846(2, 8) == 256

def test_min_5847():
    assert min_5847(3, 7) == 3

def test_max_5848():
    assert max_5848(3, 7) == 7
