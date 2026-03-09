"""Tests for test module 1402 — covers src modules [5605, 5606, 5607, 5608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5605 import modulo_5605
from module_5606 import power_5606
from module_5607 import min_5607
from module_5608 import max_5608

def test_modulo_5605():
    assert modulo_5605(10, 3) == 1

def test_power_5606():
    assert power_5606(2, 8) == 256

def test_min_5607():
    assert min_5607(3, 7) == 3

def test_max_5608():
    assert max_5608(3, 7) == 7
