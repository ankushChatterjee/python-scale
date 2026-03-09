"""Tests for test module 1450 — covers src modules [5797, 5798, 5799, 5800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5797 import modulo_5797
from module_5798 import power_5798
from module_5799 import min_5799
from module_5800 import max_5800

def test_modulo_5797():
    assert modulo_5797(10, 3) == 1

def test_power_5798():
    assert power_5798(2, 8) == 256

def test_min_5799():
    assert min_5799(3, 7) == 3

def test_max_5800():
    assert max_5800(3, 7) == 7
