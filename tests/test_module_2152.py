"""Tests for test module 2152 — covers src modules [8605, 8606, 8607, 8608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8605 import modulo_8605
from module_8606 import power_8606
from module_8607 import min_8607
from module_8608 import max_8608

def test_modulo_8605():
    assert modulo_8605(10, 3) == 1

def test_power_8606():
    assert power_8606(2, 8) == 256

def test_min_8607():
    assert min_8607(3, 7) == 3

def test_max_8608():
    assert max_8608(3, 7) == 7
