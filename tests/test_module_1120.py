"""Tests for test module 1120 — covers src modules [4477, 4478, 4479, 4480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4477 import modulo_4477
from module_4478 import power_4478
from module_4479 import min_4479
from module_4480 import max_4480

def test_modulo_4477():
    assert modulo_4477(10, 3) == 1

def test_power_4478():
    assert power_4478(2, 8) == 256

def test_min_4479():
    assert min_4479(3, 7) == 3

def test_max_4480():
    assert max_4480(3, 7) == 7
