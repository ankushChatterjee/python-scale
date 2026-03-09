"""Tests for test module 2368 — covers src modules [9469, 9470, 9471, 9472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9469 import modulo_9469
from module_9470 import power_9470
from module_9471 import min_9471
from module_9472 import max_9472

def test_modulo_9469():
    assert modulo_9469(10, 3) == 1

def test_power_9470():
    assert power_9470(2, 8) == 256

def test_min_9471():
    assert min_9471(3, 7) == 3

def test_max_9472():
    assert max_9472(3, 7) == 7
