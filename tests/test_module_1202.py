"""Tests for test module 1202 — covers src modules [4805, 4806, 4807, 4808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4805 import modulo_4805
from module_4806 import power_4806
from module_4807 import min_4807
from module_4808 import max_4808

def test_modulo_4805():
    assert modulo_4805(10, 3) == 1

def test_power_4806():
    assert power_4806(2, 8) == 256

def test_min_4807():
    assert min_4807(3, 7) == 3

def test_max_4808():
    assert max_4808(3, 7) == 7
