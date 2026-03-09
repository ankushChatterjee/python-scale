"""Tests for test module 1736 — covers src modules [6941, 6942, 6943, 6944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6941 import modulo_6941
from module_6942 import power_6942
from module_6943 import min_6943
from module_6944 import max_6944

def test_modulo_6941():
    assert modulo_6941(10, 3) == 1

def test_power_6942():
    assert power_6942(2, 8) == 256

def test_min_6943():
    assert min_6943(3, 7) == 3

def test_max_6944():
    assert max_6944(3, 7) == 7
