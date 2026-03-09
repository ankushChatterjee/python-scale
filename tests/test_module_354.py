"""Tests for test module 354 — covers src modules [1413, 1414, 1415, 1416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1413 import modulo_1413
from module_1414 import power_1414
from module_1415 import min_1415
from module_1416 import max_1416

def test_modulo_1413():
    assert modulo_1413(10, 3) == 1

def test_power_1414():
    assert power_1414(2, 8) == 256

def test_min_1415():
    assert min_1415(3, 7) == 3

def test_max_1416():
    assert max_1416(3, 7) == 7
