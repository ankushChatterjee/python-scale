"""Tests for test module 604 — covers src modules [2413, 2414, 2415, 2416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2413 import modulo_2413
from module_2414 import power_2414
from module_2415 import min_2415
from module_2416 import max_2416

def test_modulo_2413():
    assert modulo_2413(10, 3) == 1

def test_power_2414():
    assert power_2414(2, 8) == 256

def test_min_2415():
    assert min_2415(3, 7) == 3

def test_max_2416():
    assert max_2416(3, 7) == 7
