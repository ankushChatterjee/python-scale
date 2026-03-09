"""Tests for test module 156 — covers src modules [621, 622, 623, 624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_621 import modulo_621
from module_622 import power_622
from module_623 import min_623
from module_624 import max_624

def test_modulo_621():
    assert modulo_621(10, 3) == 1

def test_power_622():
    assert power_622(2, 8) == 256

def test_min_623():
    assert min_623(3, 7) == 3

def test_max_624():
    assert max_624(3, 7) == 7
