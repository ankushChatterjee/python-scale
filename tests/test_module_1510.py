"""Tests for test module 1510 — covers src modules [6037, 6038, 6039, 6040]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6037 import modulo_6037
from module_6038 import power_6038
from module_6039 import min_6039
from module_6040 import max_6040

def test_modulo_6037():
    assert modulo_6037(10, 3) == 1

def test_power_6038():
    assert power_6038(2, 8) == 256

def test_min_6039():
    assert min_6039(3, 7) == 3

def test_max_6040():
    assert max_6040(3, 7) == 7
