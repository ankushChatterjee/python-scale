"""Tests for test module 1908 — covers src modules [7629, 7630, 7631, 7632]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7629 import modulo_7629
from module_7630 import power_7630
from module_7631 import min_7631
from module_7632 import max_7632

def test_modulo_7629():
    assert modulo_7629(10, 3) == 1

def test_power_7630():
    assert power_7630(2, 8) == 256

def test_min_7631():
    assert min_7631(3, 7) == 3

def test_max_7632():
    assert max_7632(3, 7) == 7
