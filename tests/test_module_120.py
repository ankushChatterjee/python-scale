"""Tests for test module 120 — covers src modules [477, 478, 479, 480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_477 import modulo_477
from module_478 import power_478
from module_479 import min_479
from module_480 import max_480

def test_modulo_477():
    assert modulo_477(10, 3) == 1

def test_power_478():
    assert power_478(2, 8) == 256

def test_min_479():
    assert min_479(3, 7) == 3

def test_max_480():
    assert max_480(3, 7) == 7
