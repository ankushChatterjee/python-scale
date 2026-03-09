"""Tests for test module 1156 — covers src modules [4621, 4622, 4623, 4624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4621 import modulo_4621
from module_4622 import power_4622
from module_4623 import min_4623
from module_4624 import max_4624

def test_modulo_4621():
    assert modulo_4621(10, 3) == 1

def test_power_4622():
    assert power_4622(2, 8) == 256

def test_min_4623():
    assert min_4623(3, 7) == 3

def test_max_4624():
    assert max_4624(3, 7) == 7
