"""Tests for test module 192 — covers src modules [765, 766, 767, 768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_765 import modulo_765
from module_766 import power_766
from module_767 import min_767
from module_768 import max_768

def test_modulo_765():
    assert modulo_765(10, 3) == 1

def test_power_766():
    assert power_766(2, 8) == 256

def test_min_767():
    assert min_767(3, 7) == 3

def test_max_768():
    assert max_768(3, 7) == 7
