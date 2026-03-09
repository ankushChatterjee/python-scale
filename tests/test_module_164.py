"""Tests for test module 164 — covers src modules [653, 654, 655, 656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_653 import modulo_653
from module_654 import power_654
from module_655 import min_655
from module_656 import max_656

def test_modulo_653():
    assert modulo_653(10, 3) == 1

def test_power_654():
    assert power_654(2, 8) == 256

def test_min_655():
    assert min_655(3, 7) == 3

def test_max_656():
    assert max_656(3, 7) == 7
