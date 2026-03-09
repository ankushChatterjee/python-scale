"""Tests for test module 2404 — covers src modules [9613, 9614, 9615, 9616]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9613 import modulo_9613
from module_9614 import power_9614
from module_9615 import min_9615
from module_9616 import max_9616

def test_modulo_9613():
    assert modulo_9613(10, 3) == 1

def test_power_9614():
    assert power_9614(2, 8) == 256

def test_min_9615():
    assert min_9615(3, 7) == 3

def test_max_9616():
    assert max_9616(3, 7) == 7
