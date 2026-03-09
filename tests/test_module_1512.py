"""Tests for test module 1512 — covers src modules [6045, 6046, 6047, 6048]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6045 import modulo_6045
from module_6046 import power_6046
from module_6047 import min_6047
from module_6048 import max_6048

def test_modulo_6045():
    assert modulo_6045(10, 3) == 1

def test_power_6046():
    assert power_6046(2, 8) == 256

def test_min_6047():
    assert min_6047(3, 7) == 3

def test_max_6048():
    assert max_6048(3, 7) == 7
