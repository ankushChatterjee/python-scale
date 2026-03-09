"""Tests for test module 962 — covers src modules [3845, 3846, 3847, 3848]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3845 import modulo_3845
from module_3846 import power_3846
from module_3847 import min_3847
from module_3848 import max_3848

def test_modulo_3845():
    assert modulo_3845(10, 3) == 1

def test_power_3846():
    assert power_3846(2, 8) == 256

def test_min_3847():
    assert min_3847(3, 7) == 3

def test_max_3848():
    assert max_3848(3, 7) == 7
