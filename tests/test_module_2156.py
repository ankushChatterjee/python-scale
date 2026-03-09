"""Tests for test module 2156 — covers src modules [8621, 8622, 8623, 8624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8621 import modulo_8621
from module_8622 import power_8622
from module_8623 import min_8623
from module_8624 import max_8624

def test_modulo_8621():
    assert modulo_8621(10, 3) == 1

def test_power_8622():
    assert power_8622(2, 8) == 256

def test_min_8623():
    assert min_8623(3, 7) == 3

def test_max_8624():
    assert max_8624(3, 7) == 7
