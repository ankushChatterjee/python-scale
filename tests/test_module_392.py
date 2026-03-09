"""Tests for test module 392 — covers src modules [1565, 1566, 1567, 1568]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1565 import modulo_1565
from module_1566 import power_1566
from module_1567 import min_1567
from module_1568 import max_1568

def test_modulo_1565():
    assert modulo_1565(10, 3) == 1

def test_power_1566():
    assert power_1566(2, 8) == 256

def test_min_1567():
    assert min_1567(3, 7) == 3

def test_max_1568():
    assert max_1568(3, 7) == 7
