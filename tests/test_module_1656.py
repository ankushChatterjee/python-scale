"""Tests for test module 1656 — covers src modules [6621, 6622, 6623, 6624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6621 import modulo_6621
from module_6622 import power_6622
from module_6623 import min_6623
from module_6624 import max_6624

def test_modulo_6621():
    assert modulo_6621(10, 3) == 1

def test_power_6622():
    assert power_6622(2, 8) == 256

def test_min_6623():
    assert min_6623(3, 7) == 3

def test_max_6624():
    assert max_6624(3, 7) == 7
