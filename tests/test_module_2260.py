"""Tests for test module 2260 — covers src modules [9037, 9038, 9039, 9040]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9037 import modulo_9037
from module_9038 import power_9038
from module_9039 import min_9039
from module_9040 import max_9040

def test_modulo_9037():
    assert modulo_9037(10, 3) == 1

def test_power_9038():
    assert power_9038(2, 8) == 256

def test_min_9039():
    assert min_9039(3, 7) == 3

def test_max_9040():
    assert max_9040(3, 7) == 7
