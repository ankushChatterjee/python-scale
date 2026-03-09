"""Tests for test module 2354 — covers src modules [9413, 9414, 9415, 9416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9413 import modulo_9413
from module_9414 import power_9414
from module_9415 import min_9415
from module_9416 import max_9416

def test_modulo_9413():
    assert modulo_9413(10, 3) == 1

def test_power_9414():
    assert power_9414(2, 8) == 256

def test_min_9415():
    assert min_9415(3, 7) == 3

def test_max_9416():
    assert max_9416(3, 7) == 7
