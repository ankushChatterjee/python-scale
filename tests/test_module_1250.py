"""Tests for test module 1250 — covers src modules [4997, 4998, 4999, 5000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4997 import modulo_4997
from module_4998 import power_4998
from module_4999 import min_4999
from module_5000 import max_5000

def test_modulo_4997():
    assert modulo_4997(10, 3) == 1

def test_power_4998():
    assert power_4998(2, 8) == 256

def test_min_4999():
    assert min_4999(3, 7) == 3

def test_max_5000():
    assert max_5000(3, 7) == 7
