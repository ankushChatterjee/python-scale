"""Tests for test module 1486 — covers src modules [5941, 5942, 5943, 5944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5941 import modulo_5941
from module_5942 import power_5942
from module_5943 import min_5943
from module_5944 import max_5944

def test_modulo_5941():
    assert modulo_5941(10, 3) == 1

def test_power_5942():
    assert power_5942(2, 8) == 256

def test_min_5943():
    assert min_5943(3, 7) == 3

def test_max_5944():
    assert max_5944(3, 7) == 7
