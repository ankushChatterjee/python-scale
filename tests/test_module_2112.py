"""Tests for test module 2112 — covers src modules [8445, 8446, 8447, 8448]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8445 import modulo_8445
from module_8446 import power_8446
from module_8447 import min_8447
from module_8448 import max_8448

def test_modulo_8445():
    assert modulo_8445(10, 3) == 1

def test_power_8446():
    assert power_8446(2, 8) == 256

def test_min_8447():
    assert min_8447(3, 7) == 3

def test_max_8448():
    assert max_8448(3, 7) == 7
