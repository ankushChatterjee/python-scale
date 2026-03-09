"""Tests for test module 1364 — covers src modules [5453, 5454, 5455, 5456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5453 import modulo_5453
from module_5454 import power_5454
from module_5455 import min_5455
from module_5456 import max_5456

def test_modulo_5453():
    assert modulo_5453(10, 3) == 1

def test_power_5454():
    assert power_5454(2, 8) == 256

def test_min_5455():
    assert min_5455(3, 7) == 3

def test_max_5456():
    assert max_5456(3, 7) == 7
