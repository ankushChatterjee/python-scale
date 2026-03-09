"""Tests for test module 2444 — covers src modules [9773, 9774, 9775, 9776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9773 import modulo_9773
from module_9774 import power_9774
from module_9775 import min_9775
from module_9776 import max_9776

def test_modulo_9773():
    assert modulo_9773(10, 3) == 1

def test_power_9774():
    assert power_9774(2, 8) == 256

def test_min_9775():
    assert min_9775(3, 7) == 3

def test_max_9776():
    assert max_9776(3, 7) == 7
