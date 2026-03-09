"""Tests for test module 1892 — covers src modules [7565, 7566, 7567, 7568]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7565 import modulo_7565
from module_7566 import power_7566
from module_7567 import min_7567
from module_7568 import max_7568

def test_modulo_7565():
    assert modulo_7565(10, 3) == 1

def test_power_7566():
    assert power_7566(2, 8) == 256

def test_min_7567():
    assert min_7567(3, 7) == 3

def test_max_7568():
    assert max_7568(3, 7) == 7
