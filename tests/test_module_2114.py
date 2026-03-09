"""Tests for test module 2114 — covers src modules [8453, 8454, 8455, 8456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8453 import modulo_8453
from module_8454 import power_8454
from module_8455 import min_8455
from module_8456 import max_8456

def test_modulo_8453():
    assert modulo_8453(10, 3) == 1

def test_power_8454():
    assert power_8454(2, 8) == 256

def test_min_8455():
    assert min_8455(3, 7) == 3

def test_max_8456():
    assert max_8456(3, 7) == 7
