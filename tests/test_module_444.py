"""Tests for test module 444 — covers src modules [1773, 1774, 1775, 1776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1773 import modulo_1773
from module_1774 import power_1774
from module_1775 import min_1775
from module_1776 import max_1776

def test_modulo_1773():
    assert modulo_1773(10, 3) == 1

def test_power_1774():
    assert power_1774(2, 8) == 256

def test_min_1775():
    assert min_1775(3, 7) == 3

def test_max_1776():
    assert max_1776(3, 7) == 7
