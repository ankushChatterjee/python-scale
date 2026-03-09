"""Tests for test module 1380 — covers src modules [5517, 5518, 5519, 5520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5517 import modulo_5517
from module_5518 import power_5518
from module_5519 import min_5519
from module_5520 import max_5520

def test_modulo_5517():
    assert modulo_5517(10, 3) == 1

def test_power_5518():
    assert power_5518(2, 8) == 256

def test_min_5519():
    assert min_5519(3, 7) == 3

def test_max_5520():
    assert max_5520(3, 7) == 7
