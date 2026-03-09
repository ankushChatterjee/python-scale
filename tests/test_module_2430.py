"""Tests for test module 2430 — covers src modules [9717, 9718, 9719, 9720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9717 import modulo_9717
from module_9718 import power_9718
from module_9719 import min_9719
from module_9720 import max_9720

def test_modulo_9717():
    assert modulo_9717(10, 3) == 1

def test_power_9718():
    assert power_9718(2, 8) == 256

def test_min_9719():
    assert min_9719(3, 7) == 3

def test_max_9720():
    assert max_9720(3, 7) == 7
