"""Tests for test module 2236 — covers src modules [8941, 8942, 8943, 8944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8941 import modulo_8941
from module_8942 import power_8942
from module_8943 import min_8943
from module_8944 import max_8944

def test_modulo_8941():
    assert modulo_8941(10, 3) == 1

def test_power_8942():
    assert power_8942(2, 8) == 256

def test_min_8943():
    assert min_8943(3, 7) == 3

def test_max_8944():
    assert max_8944(3, 7) == 7
