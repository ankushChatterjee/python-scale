"""Tests for test module 114 — covers src modules [453, 454, 455, 456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_453 import modulo_453
from module_454 import power_454
from module_455 import min_455
from module_456 import max_456

def test_modulo_453():
    assert modulo_453(10, 3) == 1

def test_power_454():
    assert power_454(2, 8) == 256

def test_min_455():
    assert min_455(3, 7) == 3

def test_max_456():
    assert max_456(3, 7) == 7
