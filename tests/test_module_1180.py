"""Tests for test module 1180 — covers src modules [4717, 4718, 4719, 4720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4717 import modulo_4717
from module_4718 import power_4718
from module_4719 import min_4719
from module_4720 import max_4720

def test_modulo_4717():
    assert modulo_4717(10, 3) == 1

def test_power_4718():
    assert power_4718(2, 8) == 256

def test_min_4719():
    assert min_4719(3, 7) == 3

def test_max_4720():
    assert max_4720(3, 7) == 7
