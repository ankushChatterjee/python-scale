"""Tests for test module 1870 — covers src modules [7477, 7478, 7479, 7480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7477 import modulo_7477
from module_7478 import power_7478
from module_7479 import min_7479
from module_7480 import max_7480

def test_modulo_7477():
    assert modulo_7477(10, 3) == 1

def test_power_7478():
    assert power_7478(2, 8) == 256

def test_min_7479():
    assert min_7479(3, 7) == 3

def test_max_7480():
    assert max_7480(3, 7) == 7
