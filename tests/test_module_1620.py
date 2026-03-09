"""Tests for test module 1620 — covers src modules [6477, 6478, 6479, 6480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6477 import modulo_6477
from module_6478 import power_6478
from module_6479 import min_6479
from module_6480 import max_6480

def test_modulo_6477():
    assert modulo_6477(10, 3) == 1

def test_power_6478():
    assert power_6478(2, 8) == 256

def test_min_6479():
    assert min_6479(3, 7) == 3

def test_max_6480():
    assert max_6480(3, 7) == 7
