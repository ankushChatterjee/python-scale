"""Tests for test module 1944 — covers src modules [7773, 7774, 7775, 7776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7773 import modulo_7773
from module_7774 import power_7774
from module_7775 import min_7775
from module_7776 import max_7776

def test_modulo_7773():
    assert modulo_7773(10, 3) == 1

def test_power_7774():
    assert power_7774(2, 8) == 256

def test_min_7775():
    assert min_7775(3, 7) == 3

def test_max_7776():
    assert max_7776(3, 7) == 7
