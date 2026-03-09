"""Tests for test module 1904 — covers src modules [7613, 7614, 7615, 7616]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7613 import modulo_7613
from module_7614 import power_7614
from module_7615 import min_7615
from module_7616 import max_7616

def test_modulo_7613():
    assert modulo_7613(10, 3) == 1

def test_power_7614():
    assert power_7614(2, 8) == 256

def test_min_7615():
    assert min_7615(3, 7) == 3

def test_max_7616():
    assert max_7616(3, 7) == 7
