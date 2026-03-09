"""Tests for test module 688 — covers src modules [2749, 2750, 2751, 2752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2749 import modulo_2749
from module_2750 import power_2750
from module_2751 import min_2751
from module_2752 import max_2752

def test_modulo_2749():
    assert modulo_2749(10, 3) == 1

def test_power_2750():
    assert power_2750(2, 8) == 256

def test_min_2751():
    assert min_2751(3, 7) == 3

def test_max_2752():
    assert max_2752(3, 7) == 7
