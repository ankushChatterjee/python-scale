"""Tests for test module 1154 — covers src modules [4613, 4614, 4615, 4616]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4613 import modulo_4613
from module_4614 import power_4614
from module_4615 import min_4615
from module_4616 import max_4616

def test_modulo_4613():
    assert modulo_4613(10, 3) == 1

def test_power_4614():
    assert power_4614(2, 8) == 256

def test_min_4615():
    assert min_4615(3, 7) == 3

def test_max_4616():
    assert max_4616(3, 7) == 7
