"""Tests for test module 1654 — covers src modules [6613, 6614, 6615, 6616]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6613 import modulo_6613
from module_6614 import power_6614
from module_6615 import min_6615
from module_6616 import max_6616

def test_modulo_6613():
    assert modulo_6613(10, 3) == 1

def test_power_6614():
    assert power_6614(2, 8) == 256

def test_min_6615():
    assert min_6615(3, 7) == 3

def test_max_6616():
    assert max_6616(3, 7) == 7
