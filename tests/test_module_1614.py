"""Tests for test module 1614 — covers src modules [6453, 6454, 6455, 6456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6453 import modulo_6453
from module_6454 import power_6454
from module_6455 import min_6455
from module_6456 import max_6456

def test_modulo_6453():
    assert modulo_6453(10, 3) == 1

def test_power_6454():
    assert power_6454(2, 8) == 256

def test_min_6455():
    assert min_6455(3, 7) == 3

def test_max_6456():
    assert max_6456(3, 7) == 7
