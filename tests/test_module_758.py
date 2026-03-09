"""Tests for test module 758 — covers src modules [3029, 3030, 3031, 3032]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3029 import modulo_3029
from module_3030 import power_3030
from module_3031 import min_3031
from module_3032 import max_3032

def test_modulo_3029():
    assert modulo_3029(10, 3) == 1

def test_power_3030():
    assert power_3030(2, 8) == 256

def test_min_3031():
    assert min_3031(3, 7) == 3

def test_max_3032():
    assert max_3032(3, 7) == 7
