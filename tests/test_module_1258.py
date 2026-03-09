"""Tests for test module 1258 — covers src modules [5029, 5030, 5031, 5032]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5029 import modulo_5029
from module_5030 import power_5030
from module_5031 import min_5031
from module_5032 import max_5032

def test_modulo_5029():
    assert modulo_5029(10, 3) == 1

def test_power_5030():
    assert power_5030(2, 8) == 256

def test_min_5031():
    assert min_5031(3, 7) == 3

def test_max_5032():
    assert max_5032(3, 7) == 7
