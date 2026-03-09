"""Tests for test module 866 — covers src modules [3461, 3462, 3463, 3464]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3461 import modulo_3461
from module_3462 import power_3462
from module_3463 import min_3463
from module_3464 import max_3464

def test_modulo_3461():
    assert modulo_3461(10, 3) == 1

def test_power_3462():
    assert power_3462(2, 8) == 256

def test_min_3463():
    assert min_3463(3, 7) == 3

def test_max_3464():
    assert max_3464(3, 7) == 7
