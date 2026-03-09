"""Tests for test module 1786 — covers src modules [7141, 7142, 7143, 7144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7141 import modulo_7141
from module_7142 import power_7142
from module_7143 import min_7143
from module_7144 import max_7144

def test_modulo_7141():
    assert modulo_7141(10, 3) == 1

def test_power_7142():
    assert power_7142(2, 8) == 256

def test_min_7143():
    assert min_7143(3, 7) == 3

def test_max_7144():
    assert max_7144(3, 7) == 7
