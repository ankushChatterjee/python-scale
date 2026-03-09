"""Tests for test module 1392 — covers src modules [5565, 5566, 5567, 5568]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5565 import modulo_5565
from module_5566 import power_5566
from module_5567 import min_5567
from module_5568 import max_5568

def test_modulo_5565():
    assert modulo_5565(10, 3) == 1

def test_power_5566():
    assert power_5566(2, 8) == 256

def test_min_5567():
    assert min_5567(3, 7) == 3

def test_max_5568():
    assert max_5568(3, 7) == 7
