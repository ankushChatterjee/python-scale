"""Tests for test module 2120 — covers src modules [8477, 8478, 8479, 8480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8477 import modulo_8477
from module_8478 import power_8478
from module_8479 import min_8479
from module_8480 import max_8480

def test_modulo_8477():
    assert modulo_8477(10, 3) == 1

def test_power_8478():
    assert power_8478(2, 8) == 256

def test_min_8479():
    assert min_8479(3, 7) == 3

def test_max_8480():
    assert max_8480(3, 7) == 7
