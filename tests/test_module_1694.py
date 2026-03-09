"""Tests for test module 1694 — covers src modules [6773, 6774, 6775, 6776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6773 import modulo_6773
from module_6774 import power_6774
from module_6775 import min_6775
from module_6776 import max_6776

def test_modulo_6773():
    assert modulo_6773(10, 3) == 1

def test_power_6774():
    assert power_6774(2, 8) == 256

def test_min_6775():
    assert min_6775(3, 7) == 3

def test_max_6776():
    assert max_6776(3, 7) == 7
