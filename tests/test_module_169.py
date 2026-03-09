"""Tests for test module 169 — covers src modules [673, 674, 675, 676]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_673 import add_673
from module_674 import subtract_674
from module_675 import multiply_675
from module_676 import divide_676

def test_add_673():
    assert add_673(2, 3) == 5

def test_subtract_674():
    assert subtract_674(10, 4) == 6

def test_multiply_675():
    assert multiply_675(3, 7) == 21

def test_divide_676():
    assert divide_676(10, 2) == 5.0
