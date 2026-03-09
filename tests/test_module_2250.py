"""Tests for test module 2250 — covers src modules [8997, 8998, 8999, 9000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8997 import modulo_8997
from module_8998 import power_8998
from module_8999 import min_8999
from module_9000 import max_9000

def test_modulo_8997():
    assert modulo_8997(10, 3) == 1

def test_power_8998():
    assert power_8998(2, 8) == 256

def test_min_8999():
    assert min_8999(3, 7) == 3

def test_max_9000():
    assert max_9000(3, 7) == 7
