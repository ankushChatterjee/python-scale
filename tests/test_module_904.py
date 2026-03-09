"""Tests for test module 904 — covers src modules [3613, 3614, 3615, 3616]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3613 import modulo_3613
from module_3614 import power_3614
from module_3615 import min_3615
from module_3616 import max_3616

def test_modulo_3613():
    assert modulo_3613(10, 3) == 1

def test_power_3614():
    assert power_3614(2, 8) == 256

def test_min_3615():
    assert min_3615(3, 7) == 3

def test_max_3616():
    assert max_3616(3, 7) == 7
