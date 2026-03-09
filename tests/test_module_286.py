"""Tests for test module 286 — covers src modules [1141, 1142, 1143, 1144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1141 import modulo_1141
from module_1142 import power_1142
from module_1143 import min_1143
from module_1144 import max_1144

def test_modulo_1141():
    assert modulo_1141(10, 3) == 1

def test_power_1142():
    assert power_1142(2, 8) == 256

def test_min_1143():
    assert min_1143(3, 7) == 3

def test_max_1144():
    assert max_1144(3, 7) == 7
