"""Tests for test module 614 — covers src modules [2453, 2454, 2455, 2456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2453 import modulo_2453
from module_2454 import power_2454
from module_2455 import min_2455
from module_2456 import max_2456

def test_modulo_2453():
    assert modulo_2453(10, 3) == 1

def test_power_2454():
    assert power_2454(2, 8) == 256

def test_min_2455():
    assert min_2455(3, 7) == 3

def test_max_2456():
    assert max_2456(3, 7) == 7
