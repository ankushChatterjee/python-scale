"""Tests for test module 2364 — covers src modules [9453, 9454, 9455, 9456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9453 import modulo_9453
from module_9454 import power_9454
from module_9455 import min_9455
from module_9456 import max_9456

def test_modulo_9453():
    assert modulo_9453(10, 3) == 1

def test_power_9454():
    assert power_9454(2, 8) == 256

def test_min_9455():
    assert min_9455(3, 7) == 3

def test_max_9456():
    assert max_9456(3, 7) == 7
