"""Tests for test module 2104 — covers src modules [8413, 8414, 8415, 8416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8413 import modulo_8413
from module_8414 import power_8414
from module_8415 import min_8415
from module_8416 import max_8416

def test_modulo_8413():
    assert modulo_8413(10, 3) == 1

def test_power_8414():
    assert power_8414(2, 8) == 256

def test_min_8415():
    assert min_8415(3, 7) == 3

def test_max_8416():
    assert max_8416(3, 7) == 7
