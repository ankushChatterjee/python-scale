"""Tests for test module 180 — covers src modules [717, 718, 719, 720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_717 import modulo_717
from module_718 import power_718
from module_719 import min_719
from module_720 import max_720

def test_modulo_717():
    assert modulo_717(10, 3) == 1

def test_power_718():
    assert power_718(2, 8) == 256

def test_min_719():
    assert min_719(3, 7) == 3

def test_max_720():
    assert max_720(3, 7) == 7
