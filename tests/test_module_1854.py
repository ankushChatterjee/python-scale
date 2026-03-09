"""Tests for test module 1854 — covers src modules [7413, 7414, 7415, 7416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7413 import modulo_7413
from module_7414 import power_7414
from module_7415 import min_7415
from module_7416 import max_7416

def test_modulo_7413():
    assert modulo_7413(10, 3) == 1

def test_power_7414():
    assert power_7414(2, 8) == 256

def test_min_7415():
    assert min_7415(3, 7) == 3

def test_max_7416():
    assert max_7416(3, 7) == 7
