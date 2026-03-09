"""Tests for test module 1194 — covers src modules [4773, 4774, 4775, 4776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4773 import modulo_4773
from module_4774 import power_4774
from module_4775 import min_4775
from module_4776 import max_4776

def test_modulo_4773():
    assert modulo_4773(10, 3) == 1

def test_power_4774():
    assert power_4774(2, 8) == 256

def test_min_4775():
    assert min_4775(3, 7) == 3

def test_max_4776():
    assert max_4776(3, 7) == 7
