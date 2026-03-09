"""Tests for test module 236 — covers src modules [941, 942, 943, 944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_941 import modulo_941
from module_942 import power_942
from module_943 import min_943
from module_944 import max_944

def test_modulo_941():
    assert modulo_941(10, 3) == 1

def test_power_942():
    assert power_942(2, 8) == 256

def test_min_943():
    assert min_943(3, 7) == 3

def test_max_944():
    assert max_944(3, 7) == 7
