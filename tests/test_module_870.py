"""Tests for test module 870 — covers src modules [3477, 3478, 3479, 3480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3477 import modulo_3477
from module_3478 import power_3478
from module_3479 import min_3479
from module_3480 import max_3480

def test_modulo_3477():
    assert modulo_3477(10, 3) == 1

def test_power_3478():
    assert power_3478(2, 8) == 256

def test_min_3479():
    assert min_3479(3, 7) == 3

def test_max_3480():
    assert max_3480(3, 7) == 7
