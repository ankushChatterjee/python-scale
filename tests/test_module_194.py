"""Tests for test module 194 — covers src modules [773, 774, 775, 776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_773 import modulo_773
from module_774 import power_774
from module_775 import min_775
from module_776 import max_776

def test_modulo_773():
    assert modulo_773(10, 3) == 1

def test_power_774():
    assert power_774(2, 8) == 256

def test_min_775():
    assert min_775(3, 7) == 3

def test_max_776():
    assert max_776(3, 7) == 7
