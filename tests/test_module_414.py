"""Tests for test module 414 — covers src modules [1653, 1654, 1655, 1656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1653 import modulo_1653
from module_1654 import power_1654
from module_1655 import min_1655
from module_1656 import max_1656

def test_modulo_1653():
    assert modulo_1653(10, 3) == 1

def test_power_1654():
    assert power_1654(2, 8) == 256

def test_min_1655():
    assert min_1655(3, 7) == 3

def test_max_1656():
    assert max_1656(3, 7) == 7
