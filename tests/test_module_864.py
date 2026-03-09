"""Tests for test module 864 — covers src modules [3453, 3454, 3455, 3456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3453 import modulo_3453
from module_3454 import power_3454
from module_3455 import min_3455
from module_3456 import max_3456

def test_modulo_3453():
    assert modulo_3453(10, 3) == 1

def test_power_3454():
    assert power_3454(2, 8) == 256

def test_min_3455():
    assert min_3455(3, 7) == 3

def test_max_3456():
    assert max_3456(3, 7) == 7
