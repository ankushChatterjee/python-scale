"""Tests for test module 1986 — covers src modules [7941, 7942, 7943, 7944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7941 import modulo_7941
from module_7942 import power_7942
from module_7943 import min_7943
from module_7944 import max_7944

def test_modulo_7941():
    assert modulo_7941(10, 3) == 1

def test_power_7942():
    assert power_7942(2, 8) == 256

def test_min_7943():
    assert min_7943(3, 7) == 3

def test_max_7944():
    assert max_7944(3, 7) == 7
