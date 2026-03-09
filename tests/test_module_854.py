"""Tests for test module 854 — covers src modules [3413, 3414, 3415, 3416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3413 import modulo_3413
from module_3414 import power_3414
from module_3415 import min_3415
from module_3416 import max_3416

def test_modulo_3413():
    assert modulo_3413(10, 3) == 1

def test_power_3414():
    assert power_3414(2, 8) == 256

def test_min_3415():
    assert min_3415(3, 7) == 3

def test_max_3416():
    assert max_3416(3, 7) == 7
