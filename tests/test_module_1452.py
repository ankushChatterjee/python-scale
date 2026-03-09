"""Tests for test module 1452 — covers src modules [5805, 5806, 5807, 5808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5805 import modulo_5805
from module_5806 import power_5806
from module_5807 import min_5807
from module_5808 import max_5808

def test_modulo_5805():
    assert modulo_5805(10, 3) == 1

def test_power_5806():
    assert power_5806(2, 8) == 256

def test_min_5807():
    assert min_5807(3, 7) == 3

def test_max_5808():
    assert max_5808(3, 7) == 7
