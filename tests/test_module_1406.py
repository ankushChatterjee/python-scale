"""Tests for test module 1406 — covers src modules [5621, 5622, 5623, 5624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5621 import modulo_5621
from module_5622 import power_5622
from module_5623 import min_5623
from module_5624 import max_5624

def test_modulo_5621():
    assert modulo_5621(10, 3) == 1

def test_power_5622():
    assert power_5622(2, 8) == 256

def test_min_5623():
    assert min_5623(3, 7) == 3

def test_max_5624():
    assert max_5624(3, 7) == 7
