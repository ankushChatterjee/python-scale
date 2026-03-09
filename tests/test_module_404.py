"""Tests for test module 404 — covers src modules [1613, 1614, 1615, 1616]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1613 import modulo_1613
from module_1614 import power_1614
from module_1615 import min_1615
from module_1616 import max_1616

def test_modulo_1613():
    assert modulo_1613(10, 3) == 1

def test_power_1614():
    assert power_1614(2, 8) == 256

def test_min_1615():
    assert min_1615(3, 7) == 3

def test_max_1616():
    assert max_1616(3, 7) == 7
