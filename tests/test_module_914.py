"""Tests for test module 914 — covers src modules [3653, 3654, 3655, 3656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3653 import modulo_3653
from module_3654 import power_3654
from module_3655 import min_3655
from module_3656 import max_3656

def test_modulo_3653():
    assert modulo_3653(10, 3) == 1

def test_power_3654():
    assert power_3654(2, 8) == 256

def test_min_3655():
    assert min_3655(3, 7) == 3

def test_max_3656():
    assert max_3656(3, 7) == 7
