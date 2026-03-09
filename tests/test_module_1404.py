"""Tests for test module 1404 — covers src modules [5613, 5614, 5615, 5616]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5613 import modulo_5613
from module_5614 import power_5614
from module_5615 import min_5615
from module_5616 import max_5616

def test_modulo_5613():
    assert modulo_5613(10, 3) == 1

def test_power_5614():
    assert power_5614(2, 8) == 256

def test_min_5615():
    assert min_5615(3, 7) == 3

def test_max_5616():
    assert max_5616(3, 7) == 7
