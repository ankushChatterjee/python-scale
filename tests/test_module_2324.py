"""Tests for test module 2324 — covers src modules [9293, 9294, 9295, 9296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9293 import modulo_9293
from module_9294 import power_9294
from module_9295 import min_9295
from module_9296 import max_9296

def test_modulo_9293():
    assert modulo_9293(10, 3) == 1

def test_power_9294():
    assert power_9294(2, 8) == 256

def test_min_9295():
    assert min_9295(3, 7) == 3

def test_max_9296():
    assert max_9296(3, 7) == 7
