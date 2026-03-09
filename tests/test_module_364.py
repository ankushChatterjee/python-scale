"""Tests for test module 364 — covers src modules [1453, 1454, 1455, 1456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1453 import modulo_1453
from module_1454 import power_1454
from module_1455 import min_1455
from module_1456 import max_1456

def test_modulo_1453():
    assert modulo_1453(10, 3) == 1

def test_power_1454():
    assert power_1454(2, 8) == 256

def test_min_1455():
    assert min_1455(3, 7) == 3

def test_max_1456():
    assert max_1456(3, 7) == 7
