"""Tests for test module 1208 — covers src modules [4829, 4830, 4831, 4832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4829 import modulo_4829
from module_4830 import power_4830
from module_4831 import min_4831
from module_4832 import max_4832

def test_modulo_4829():
    assert modulo_4829(10, 3) == 1

def test_power_4830():
    assert power_4830(2, 8) == 256

def test_min_4831():
    assert min_4831(3, 7) == 3

def test_max_4832():
    assert max_4832(3, 7) == 7
