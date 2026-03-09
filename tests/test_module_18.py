"""Tests for test module 18 — covers src modules [69, 70, 71, 72]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_69 import modulo_69
from module_70 import power_70
from module_71 import min_71
from module_72 import max_72

def test_modulo_69():
    assert modulo_69(10, 3) == 1

def test_power_70():
    assert power_70(2, 8) == 256

def test_min_71():
    assert min_71(3, 7) == 3

def test_max_72():
    assert max_72(3, 7) == 7
