"""Tests for test module 1114 — covers src modules [4453, 4454, 4455, 4456]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4453 import modulo_4453
from module_4454 import power_4454
from module_4455 import min_4455
from module_4456 import max_4456

def test_modulo_4453():
    assert modulo_4453(10, 3) == 1

def test_power_4454():
    assert power_4454(2, 8) == 256

def test_min_4455():
    assert min_4455(3, 7) == 3

def test_max_4456():
    assert max_4456(3, 7) == 7
