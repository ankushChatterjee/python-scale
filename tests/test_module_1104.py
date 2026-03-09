"""Tests for test module 1104 — covers src modules [4413, 4414, 4415, 4416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4413 import modulo_4413
from module_4414 import power_4414
from module_4415 import min_4415
from module_4416 import max_4416

def test_modulo_4413():
    assert modulo_4413(10, 3) == 1

def test_power_4414():
    assert power_4414(2, 8) == 256

def test_min_4415():
    assert min_4415(3, 7) == 3

def test_max_4416():
    assert max_4416(3, 7) == 7
