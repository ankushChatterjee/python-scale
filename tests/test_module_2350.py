"""Tests for test module 2350 — covers src modules [9397, 9398, 9399, 9400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9397 import modulo_9397
from module_9398 import power_9398
from module_9399 import min_9399
from module_9400 import max_9400

def test_modulo_9397():
    assert modulo_9397(10, 3) == 1

def test_power_9398():
    assert power_9398(2, 8) == 256

def test_min_9399():
    assert min_9399(3, 7) == 3

def test_max_9400():
    assert max_9400(3, 7) == 7
