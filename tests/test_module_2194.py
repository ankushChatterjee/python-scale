"""Tests for test module 2194 — covers src modules [8773, 8774, 8775, 8776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8773 import modulo_8773
from module_8774 import power_8774
from module_8775 import min_8775
from module_8776 import max_8776

def test_modulo_8773():
    assert modulo_8773(10, 3) == 1

def test_power_8774():
    assert power_8774(2, 8) == 256

def test_min_8775():
    assert min_8775(3, 7) == 3

def test_max_8776():
    assert max_8776(3, 7) == 7
