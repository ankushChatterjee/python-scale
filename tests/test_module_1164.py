"""Tests for test module 1164 — covers src modules [4653, 4654, 4655, 4656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4653 import modulo_4653
from module_4654 import power_4654
from module_4655 import min_4655
from module_4656 import max_4656

def test_modulo_4653():
    assert modulo_4653(10, 3) == 1

def test_power_4654():
    assert power_4654(2, 8) == 256

def test_min_4655():
    assert min_4655(3, 7) == 3

def test_max_4656():
    assert max_4656(3, 7) == 7
