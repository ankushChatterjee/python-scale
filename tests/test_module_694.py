"""Tests for test module 694 — covers src modules [2773, 2774, 2775, 2776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2773 import modulo_2773
from module_2774 import power_2774
from module_2775 import min_2775
from module_2776 import max_2776

def test_modulo_2773():
    assert modulo_2773(10, 3) == 1

def test_power_2774():
    assert power_2774(2, 8) == 256

def test_min_2775():
    assert min_2775(3, 7) == 3

def test_max_2776():
    assert max_2776(3, 7) == 7
