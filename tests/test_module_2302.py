"""Tests for test module 2302 — covers src modules [9205, 9206, 9207, 9208]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9205 import modulo_9205
from module_9206 import power_9206
from module_9207 import min_9207
from module_9208 import max_9208

def test_modulo_9205():
    assert modulo_9205(10, 3) == 1

def test_power_9206():
    assert power_9206(2, 8) == 256

def test_min_9207():
    assert min_9207(3, 7) == 3

def test_max_9208():
    assert max_9208(3, 7) == 7
