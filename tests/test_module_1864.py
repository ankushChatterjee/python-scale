"""Tests for test module 1864 — covers src modules [7453, 7454, 7455, 7456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7453 import modulo_7453
from module_7454 import power_7454
from module_7455 import min_7455
from module_7456 import max_7456

def test_modulo_7453():
    assert modulo_7453(10, 3) == 1

def test_power_7454():
    assert power_7454(2, 8) == 256

def test_min_7455():
    assert min_7455(3, 7) == 3

def test_max_7456():
    assert max_7456(3, 7) == 7
