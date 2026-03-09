"""Tests for test module 258 — covers src modules [1029, 1030, 1031, 1032]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1029 import modulo_1029
from module_1030 import power_1030
from module_1031 import min_1031
from module_1032 import max_1032

def test_modulo_1029():
    assert modulo_1029(10, 3) == 1

def test_power_1030():
    assert power_1030(2, 8) == 256

def test_min_1031():
    assert min_1031(3, 7) == 3

def test_max_1032():
    assert max_1032(3, 7) == 7
