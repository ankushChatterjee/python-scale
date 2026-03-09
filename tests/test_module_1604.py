"""Tests for test module 1604 — covers src modules [6413, 6414, 6415, 6416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6413 import modulo_6413
from module_6414 import power_6414
from module_6415 import min_6415
from module_6416 import max_6416

def test_modulo_6413():
    assert modulo_6413(10, 3) == 1

def test_power_6414():
    assert power_6414(2, 8) == 256

def test_min_6415():
    assert min_6415(3, 7) == 3

def test_max_6416():
    assert max_6416(3, 7) == 7
