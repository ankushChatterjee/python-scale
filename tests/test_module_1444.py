"""Tests for test module 1444 — covers src modules [5773, 5774, 5775, 5776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5773 import modulo_5773
from module_5774 import power_5774
from module_5775 import min_5775
from module_5776 import max_5776

def test_modulo_5773():
    assert modulo_5773(10, 3) == 1

def test_power_5774():
    assert power_5774(2, 8) == 256

def test_min_5775():
    assert min_5775(3, 7) == 3

def test_max_5776():
    assert max_5776(3, 7) == 7
