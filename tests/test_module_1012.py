"""Tests for test module 1012 — covers src modules [4045, 4046, 4047, 4048]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4045 import modulo_4045
from module_4046 import power_4046
from module_4047 import min_4047
from module_4048 import max_4048

def test_modulo_4045():
    assert modulo_4045(10, 3) == 1

def test_power_4046():
    assert power_4046(2, 8) == 256

def test_min_4047():
    assert min_4047(3, 7) == 3

def test_max_4048():
    assert max_4048(3, 7) == 7
