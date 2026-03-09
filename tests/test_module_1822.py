"""Tests for test module 1822 — covers src modules [7285, 7286, 7287, 7288]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7285 import modulo_7285
from module_7286 import power_7286
from module_7287 import min_7287
from module_7288 import max_7288

def test_modulo_7285():
    assert modulo_7285(10, 3) == 1

def test_power_7286():
    assert power_7286(2, 8) == 256

def test_min_7287():
    assert min_7287(3, 7) == 3

def test_max_7288():
    assert max_7288(3, 7) == 7
