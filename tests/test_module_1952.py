"""Tests for test module 1952 — covers src modules [7805, 7806, 7807, 7808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7805 import modulo_7805
from module_7806 import power_7806
from module_7807 import min_7807
from module_7808 import max_7808

def test_modulo_7805():
    assert modulo_7805(10, 3) == 1

def test_power_7806():
    assert power_7806(2, 8) == 256

def test_min_7807():
    assert min_7807(3, 7) == 3

def test_max_7808():
    assert max_7808(3, 7) == 7
