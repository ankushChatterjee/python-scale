"""Tests for test module 736 — covers src modules [2941, 2942, 2943, 2944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2941 import modulo_2941
from module_2942 import power_2942
from module_2943 import min_2943
from module_2944 import max_2944

def test_modulo_2941():
    assert modulo_2941(10, 3) == 1

def test_power_2942():
    assert power_2942(2, 8) == 256

def test_min_2943():
    assert min_2943(3, 7) == 3

def test_max_2944():
    assert max_2944(3, 7) == 7
