"""Tests for test module 486 — covers src modules [1941, 1942, 1943, 1944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1941 import modulo_1941
from module_1942 import power_1942
from module_1943 import min_1943
from module_1944 import max_1944

def test_modulo_1941():
    assert modulo_1941(10, 3) == 1

def test_power_1942():
    assert power_1942(2, 8) == 256

def test_min_1943():
    assert min_1943(3, 7) == 3

def test_max_1944():
    assert max_1944(3, 7) == 7
