"""Tests for test module 1192 — covers src modules [4765, 4766, 4767, 4768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4765 import modulo_4765
from module_4766 import power_4766
from module_4767 import min_4767
from module_4768 import max_4768

def test_modulo_4765():
    assert modulo_4765(10, 3) == 1

def test_power_4766():
    assert power_4766(2, 8) == 256

def test_min_4767():
    assert min_4767(3, 7) == 3

def test_max_4768():
    assert max_4768(3, 7) == 7
