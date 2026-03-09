"""Tests for test module 142 — covers src modules [565, 566, 567, 568]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_565 import modulo_565
from module_566 import power_566
from module_567 import min_567
from module_568 import max_568

def test_modulo_565():
    assert modulo_565(10, 3) == 1

def test_power_566():
    assert power_566(2, 8) == 256

def test_min_567():
    assert min_567(3, 7) == 3

def test_max_568():
    assert max_568(3, 7) == 7
