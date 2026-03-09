"""Tests for test module 986 — covers src modules [3941, 3942, 3943, 3944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3941 import modulo_3941
from module_3942 import power_3942
from module_3943 import min_3943
from module_3944 import max_3944

def test_modulo_3941():
    assert modulo_3941(10, 3) == 1

def test_power_3942():
    assert power_3942(2, 8) == 256

def test_min_3943():
    assert min_3943(3, 7) == 3

def test_max_3944():
    assert max_3944(3, 7) == 7
